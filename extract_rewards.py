import json
import re
import os

results = []

for i in range(1, 101):
    file_path = f"stage{i}.md"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find JSON block after 🎁 초등학생용 특별 보상
            reward_match = re.search(r"🎁 초등학생용 특별 보상\s+```json\s+(.*?)\s+```", content, re.DOTALL)
            if reward_match:
                try:
                    reward_json = json.loads(reward_match.group(1))
                    rewards = reward_json.get("rewards", [])
                    for r in rewards:
                        r["stage"] = i
                        results.append(r)
                except Exception as e:
                    print(f"Error parsing JSON in {file_path}: {e}")
            else:
                # Try simple reward list if JSON not found
                # Some files might have rewards in bullet points
                lines = content.split('\n')
                in_rewards = False
                for line in lines:
                    if "🎁 초등학생용 특별 보상" in line:
                        in_rewards = True
                        continue
                    if in_rewards and line.strip() == "":
                        continue
                    if in_rewards and (line.startswith("*") or line.startswith("-") or ":" in line):
                        # Example: 버디의 사탕: 버디가 기운을 내라며 반짝이는 사탕 아이템을 줍니다. (에너지 +1)
                        match = re.match(r"^\s*[\*\-]?\s*([^:]+):\s*(.*)$", line)
                        if match:
                            name = match.group(1).strip()
                            desc = match.group(2).strip()
                            reward_type = "sticker" if "스티커" in name or "뱃지" in name else "item"
                            results.append({
                                "type": reward_type,
                                "name": name,
                                "description": desc,
                                "stage": i
                            })
                    elif in_rewards and line.startswith("#"): # Next section
                        in_rewards = False
                
with open("rewards.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(results)} rewards to rewards.json")
