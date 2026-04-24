# Stage 2: 어두운 복도 (The Dark Hallway)

[상황 설명]
버디를 따라 방 밖으로 나왔어요. 복도는 아주 길고 어두워요. 버디가 당신의 얼굴을 살피며 물어봐요.

[Main Dialogue (대화)]
Buddy: "How are you? Are you okay?"
(기분이 어때? 괜찮니?)

You: "I am a little scared. It is very dark."
(조금 무서워. 너무 어둡거든.)

Buddy: "I am happy because I am with you! Look, I have a small light."
(나는 너랑 같이 있어서 기뻐! 봐봐, 나한테 작은 불빛이 있어.)

You: "That is good. I am hungry, too."
(다행이다. 나 배도 고파.)

Buddy: "Don't worry. We can find some bread soon!"
(걱정 마. 곧 빵을 찾을 수 있을 거야!)

[Stage 2 Quiz: 기분을 말해봐요!]
버디에게 당신의 상태를 정확히 알려줘야 해요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "버디가 'How are you?'라고 물었어요. 대답으로 알맞은 것은?",
      "hint": "지금 나의 상태나 기분을 말해야 해요.",
      "answerOptions": [
        { "text": "I am fine, thank you.", "isCorrect": true },
        { "text": "I am a robot.", "isCorrect": false },
        { "text": "Hello, Buddy.", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "'I am hungry.'는 무슨 뜻일까요?",
      "hint": "배에서 꼬르륵 소리가 날 때 하는 말이에요.",
      "answerOptions": [
        { "text": "졸려요.", "isCorrect": false },
        { "text": "배고파요.", "isCorrect": true },
        { "text": "심심해요.", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "버디가 'I am happy'라고 한 이유는?",
      "hint": "Buddy: 'I am happy because I am with you! '",
      "answerOptions": [
        { "text": "혼자 있어서", "isCorrect": false },
        { "text": "잠을 자서", "isCorrect": false },
        { "text": "함께 있어서", "isCorrect": true }
      ]
    }
  ]
}
```

🎁 초등학생용 특별 보상
```json
{
  "rewards": [
    {
      "type": "item",
      "id": "small_flashlight",
      "name": "작은 손전등",
      "description": "어두운 곳을 밝힐 수 있는 귀여운 손전등입니다."
    },
    {
      "type": "sticker",
      "id": "courage_badge_stage2",
      "name": "용기의 뱃지",
      "description": "\"무서움을 이겨내자!\" 뱃지를 획득했습니다."
    }
  ]
}
```
Buddy: "You are doing great! Let's keep going. Shhh, I hear a robot moving!"
(정말 잘하고 있어! 계속 가자. 쉿, 로봇이 움직이는 소리가 들려!)
