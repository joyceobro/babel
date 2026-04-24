# Stage 73: 규칙 찾기 (The First Rule)

[상황 설명]
실험실 벽에 규칙들이 적혀 있어요. 안전하게 탐험하기 위해 규칙을 꼭 지켜야 해요.

[Main Dialogue (대화)]
Buddy: "Wait! We must follow the **rules** here."
(잠깐! 여기서는 **규칙**을 따라야 해.)

You: "What is the **first rule**?"
( **첫 번째 규칙**이 뭐야?)

Buddy: "The **first rule** is 'Wear your goggles'."
( **첫 번째 규칙**은 '고글을 써라'야.)

You: "And what is the second **rule**?"
(그럼 두 번째 **규칙**은?)

Buddy: "The second **rule** is 'Don't touch the chemicals'."
(두 번째 **규칙**은 '화학 물질을 만지지 마라'야.)

You: "Okay. I will follow every **rule**."
(알았어. 모든 **규칙**을 잘 지킬게.)

[Stage 73 Quiz: 규칙을 지켜요!]
규칙과 관련된 표현을 영어로 익혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "여러 사람이 지켜야 할 '규칙'을 영어로 무엇이라고 하나요?",
      "hint : R로 시작하는 네 글자 단어예요. (Rule)",
      "answerOptions": [
        { "text": "Rule", "isCorrect": true },
        { "text": "Game", "isCorrect": false },
        { "text": "Song", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "'첫 번째 규칙'을 영어로 하면?",
      "hint": "First와 Rule을 합쳐보세요.",
      "answerOptions": [
        { "text": "First rule", "isCorrect": true },
        { "text": "One rule", "isCorrect": false },
        { "text": "Best rule", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "실험실의 첫 번째 규칙은 무엇이었나요?",
      "hint": "눈을 보호하는 장비를 써야 해요.",
      "answerOptions": [
        { "text": "Eat bread", "isCorrect": false },
        { "text": "Wear goggles", "isCorrect": true },
        { "text": "Run fast", "isCorrect": false }
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
      "id": "lab_고글",
      "name": "실험실 고글",
      "description": "눈을 안전하게 보호해주는 반짝이는 고글입니다."
    },
    {
      "type": "sticker",
      "id": "모범생_badge_stage73",
      "name": "모범생 배지",
      "description": "\"규칙을 가장 잘 지키는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"Rules keep us safe. Now we can explore the lab safely!\""
    }
  ]
}
```