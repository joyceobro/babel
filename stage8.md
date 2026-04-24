# Stage 8: 에너지 캔 사냥 (Color Hunt)

[상황 설명]
버디의 에너지가 떨어지고 있어요! 바닥에 흩어진 에너지 캔들을 색깔별로 모아야 해요.

[Main Dialogue (대화)]
Buddy: "Oh no! I need energy. Can you see the cans?"
(안돼! 에너지가 필요해. 저 캔들 보이니?)

You: "Yes! There are many colors. Which one do you want?"
(응! 색깔이 아주 많아. 어떤 걸 원해?)

Buddy: "I need the **red** one first. It's for my battery."
(먼저 **빨간색**이 필요해. 내 배터리용이야.)

You: "Here is the **red** can. What about the **blue** one?"
(여기 빨간 캔 있어. **파란색**은 어때?)

Buddy: "The **blue** can is for my legs. And the **yellow** one is for my eyes!"
(파란 캔은 내 다리용이야. 그리고 **노란색**은 내 눈을 위한 거야!)

[Stage 8 Quiz: 색깔을 맞춰봐요!]
캔의 색깔을 영어로 정확히 골라보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "사과나 딸기처럼 '빨간색'을 뜻하는 단어는?",
      "hint": "신호등의 멈춤 신호 색깔이에요.",
      "answerOptions": [
        { "text": "Red", "isCorrect": true },
        { "text": "Blue", "isCorrect": false },
        { "text": "Yellow", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "하늘이나 바다처럼 '파란색'을 뜻하는 단어는?",
      "hint": "시원한 느낌의 색깔이에요.",
      "answerOptions": [
        { "text": "Red", "isCorrect": false },
        { "text": "Blue", "isCorrect": true },
        { "text": "Yellow", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "바나나나 레몬처럼 '노란색'을 뜻하는 단어는?",
      "hint": "병아리 색깔이에요.",
      "answerOptions": [
        { "text": "Red", "isCorrect": false },
        { "text": "Blue", "isCorrect": false },
        { "text": "Yellow", "isCorrect": true }
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
      "id": "무지개_페인트",
      "name": "무지개 페인트",
      "description": "무엇이든 예쁜 색으로 칠할 수 있는 페인트 세트입니다."
    },
    {
      "type": "item",
      "id": "에너지_배터리",
      "name": "에너지 배터리",
      "description": "버디를 충전해줄 수 있는 예비 배터리입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"Thank you! I feel great now. My eyes are shining yellow!\""
    }
  ]
}
```