# Stage 6: 수수께끼 문 (The Riddle Door)

[상황 설명]
작은 로봇 하나가 문 앞에 앉아 퀴즈를 내고 있어요. 이 로봇은 우리가 무엇을 할 수 있는지 물어봐요.

[Main Dialogue (대화)]
Riddle Robot: "Can you speak English?"
(너 영어 할 줄 아니?)

You: "Yes, I can!"
(응, 할 수 있어!)

Riddle Robot: "Hmm... Can you fly like a bird?"
(흠... 너 새처럼 날 수 있니?)

You: "No, I can't. But I can run very fast."
(아니, 못 날아. 하지만 아주 빨리 달릴 수는 있어.)

Buddy: "He is very smart! He can help us."
(이 친구는 아주 똑똑해! 우리를 도울 수 있다고.)

[Stage 6 Quiz: 나는 할 수 있어요!]
당신이 할 수 있는 것과 없는 것을 영어로 대답해 보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "상대방이 '할 수 있니?'라고 물어볼 때 사용하는 말은?",
      "hint": "할 수 있다는 뜻의 조동사예요.",
      "answerOptions": [
        { "text": "Can you...?", "isCorrect": true },
        { "text": "Are you...?", "isCorrect": false },
        { "text": "Do you...?", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "'Yes, I can.'은 무슨 뜻일까요?",
      "hint": "긍정의 대답이에요.",
      "answerOptions": [
        { "text": "아니, 못 해.", "isCorrect": false },
        { "text": "응, 할 수 있어.", "isCorrect": true },
        { "text": "모르겠어.", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "새처럼 날 수 있냐는 질문에 대한 알맞은 답은?",
      "hint": "사람은 날개가 없죠?",
      "answerOptions": [
        { "text": "Yes, I can.", "isCorrect": false },
        { "text": "No, I can't.", "isCorrect": true },
        { "text": "I am a bird.", "isCorrect": false }
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
      "id": "만능_글러브",
      "name": "만능 글러브",
      "description": "무엇이든 잘 할 수 있게 도와주는 장갑입니다."
    },
    {
      "type": "item",
      "id": "자신감_물약",
      "name": "자신감 물약",
      "description": "마시면 목소리가 커지는 신비한 음료입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"The door is open! Your English is better than mine!\""
    }
  ]
}
```