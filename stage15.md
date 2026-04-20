# Stage 15: 보안실 잠입 (The Secret Code)

[상황 설명]
보안실 문 앞에 도착했어요. 경비 로봇들이 서로 숫자를 말하며 대화하고 있어요. 잘 들어보면 암호를 알 수 있을 것 같아요!

[Main Dialogue (대화)]
Guard A: "What is the secret code for today?"
(오늘의 비밀 암호가 뭐야?)

Guard B: "It's a big number. Listen. It's **two, one, five, one**."
(큰 숫자야. 잘 들어. **2, 1, 5, 1**이야.)

Buddy: "Did you hear that? **Two-one-five-one**! That's **2151**!"
(들었어? **2-1-5-1**! **2151**이래!)

You: "Yes! **Twenty-one** and **Fifty-one**? No, it's just **2151**."
(응! **21**이랑 **51**? 아니, 그냥 **2151**이네.)

Buddy: "Quick! Remember the number **2151**. We can open the door now!"
(빨리! 숫자 **2151**을 기억해. 이제 문을 열 수 있어!)

[Stage 15 Quiz: 숫자를 찾아라!]
로봇들이 말한 암호를 정확히 맞혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "경비 로봇들이 말한 네 자리 암호는?",
      "hint": "숫자 4개를 순서대로 생각해보세요.",
      "answerOptions": [
        { "text": "1234", "isCorrect": false },
        { "text": "2151", "isCorrect": true },
        { "text": "7788", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "숫자 '21'을 영어로 읽으면?",
      "hint": "Twenty... 뒤에 1을 붙여요.",
      "answerOptions": [
        { "text": "Twenty-one", "isCorrect": true },
        { "text": "Twelve", "isCorrect": false },
        { "text": "Two-one", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "숫자 '51'을 영어로 읽으면?",
      "hint": "Fifty... 뒤에 1을 붙여요.",
      "answerOptions": [
        { "text": "Fifteen", "isCorrect": false },
        { "text": "Fifty-one", "isCorrect": true },
        { "text": "Five-one", "isCorrect": false }
      ]
    }
  ]
}
```

🎁 초등학생용 특별 보상
- **숫자 암호표**: 1부터 100까지 숫자가 적힌 종이입니다.
- **보안 요원 카드**: "비밀을 알아낸 친구" 카드입니다.

Buddy: "You are a great listener! 2151 is the key. Let's type it in!"
(넌 정말 잘 듣는구나! 2151이 핵심이야. 어서 입력하자!)
