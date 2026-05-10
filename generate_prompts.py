import json

# Enhanced translation and keyword mapping based on image_guideline.md
translations = {
    "사탕": "candy", "손전등": "flashlight", "리모컨": "remote control", "신발": "shoes",
    "열쇠고리": "keychain", "스티커": "sticker", "배지": "badge", "뱃지": "badge",
    "망토": "cloak", "글러브": "gloves", "장갑": "gloves", "물약": "potion",
    "음료": "drink", "사과": "apple", "쿠키": "cookie", "동전": "coin",
    "모자": "hat", "지도": "map", "축구공": "soccer ball", "인형": "doll",
    "공": "ball", "셔츠": "shirt", "바지": "pants", "카트": "shopping cart",
    "주사위": "dice", "망치": "hammer", "청소기": "vacuum cleaner", "빗자루": "broom",
    "시계": "clock", "안경": "glasses", "망원경": "telescope", "돋보기": "magnifying glass",
    "책": "book", "연필": "pencil", "종이": "paper", "컴퓨터": "computer",
    "카메라": "camera", "드라이버": "screwdriver", "렌치": "wrench", "기어": "gear",
    "나사": "screw", "헬멧": "helmet", "티켓": "ticket", "기차": "train",
    "버스": "bus", "꽃": "flower", "나무": "tree", "잎": "leaf",
    "달력": "calendar", "우산": "umbrella", "장화": "boots", "선물": "gift",
    "케이크": "cake", "초대장": "invitation", "다이어리": "diary", "열쇠": "key",
    "카드": "card", "배터리": "battery", "에너지": "energy", "로봇": "robot",
    "강아지": "puppy", "고양이": "cat", "새": "bird", "완드": "wand", "지팡이": "staff"
}

def get_eng(text):
    for ko, en in translations.items():
        if ko in text:
            return en
    return ""

with open("rewards.json", "r", encoding="utf-8") as f:
    rewards = json.load(f)

# Filter out dialogue-like entries
rewards = [r for r in rewards if r.get("name") != "Buddy" and len(r.get("name", "")) < 20]

item_style = "Soft 2D illustration, cute stylized game icon, iridescent sheen, pastel purple and pink colors, sparkles and stars particles, white background, clean thick outlines, high quality"
sticker_style = "Circular sticker design, die-cut sticker with thick white border, flat vector illustration, cute mascot style, pastel palette, iridescent highlights, game reward sticker, isolated on white"

output = "# 아이템 및 스티커 이미지 프롬프트 정리\n\n"
output += "이 문서는 `image_guideline.md`의 시각적 스타일 가이드를 준수하여 작성되었습니다.\n"
output += "- **아이템**: 부드러운 2D 일러스트, 무지개빛 광택, 흰색 배경\n"
output += "- **스티커**: 굵은 흰색 테두리가 있는 원형/다이컷 플랫 벡터 디자인\n\n"

output += "| 스테이지 | 종류 | 이름 | 설명 | 이미지 생성 프롬프트 |\n"
output += "| :--- | :--- | :--- | :--- | :--- |\n"

for r in rewards:
    stage = r.get("stage", "?")
    rtype = "아이템" if r.get("type") == "item" else "스티커"
    name = r.get("name", "")
    desc = r.get("description", "").replace("\n", " ")
    
    eng_name = get_eng(name)
    subject = eng_name if eng_name else name
    
    if r.get("type") == "item":
        prompt = f"{subject}, {name}, {desc}, {item_style}"
    else:
        prompt = f"{subject}, {name}, {desc}, {sticker_style}"
    
    prompt = prompt.replace("|", "\\|")
    
    output += f"| {stage} | {rtype} | {name} | {desc} | {prompt} |\n"

with open("reward_prompts.md", "w", encoding="utf-8") as f:
    f.write(output)

# Update rewards.json with prompts as well for convenience
for r in rewards:
    eng_name = get_eng(r.get("name", ""))
    subject = eng_name if eng_name else r.get("name", "")
    if r.get("type") == "item":
        r["image_prompt"] = f"{subject}, {r.get('name')}, {r.get('description')}, {item_style}"
    else:
        r["image_prompt"] = f"{subject}, {r.get('name')}, {r.get('description')}, {sticker_style}"

with open("rewards.json", "w", encoding="utf-8") as f:
    json.dump(rewards, f, ensure_ascii=False, indent=2)

print(f"Updated reward_prompts.md and rewards.json with {len(rewards)} entries.")
