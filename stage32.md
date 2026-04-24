# Stage 32: 가격 물어보기 (How Much?)

[상황 설명]
물건값을 지불해야 해요. 점원 로봇에게 가격이 얼마인지 물어볼까요?

[Main Dialogue (대화)]
You: "**How much is it**? I want to pay for the apple."
( **이거 얼마예요**? 사과 값을 내고 싶어요.)

Clerk Robot: "It is **one** dollar, please."
( **1**달러입니다.)

Buddy: "What about the big cake? **How much is it**?"
(저 커다란 케이크는요? **그건 얼마예요**?)

Clerk Robot: "It is **ten** dollars. It is very expensive!"
( **10**달러예요. 아주 비싸답니다!)

You: "Wow! **Ten** dollars is a lot. Here is **one** dollar for my apple."
(와! **10**달러는 큰돈이네요. 여기 제 사과 값 **1**달러예요.)

[Stage 32 Quiz: 얼마인가요?]
가격이나 양을 물어볼 때 쓰는 핵심 표현을 배워요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "물건의 가격을 물어볼 때 쓰는 표현은?",
      "hint : How ____ is it? 빈칸에 들어갈 말은?",
      "answerOptions": [
        { "text": "many", "isCorrect": false },
        { "text": "much", "isCorrect": true },
        { "text": "old", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "사과의 가격은 얼마였나요?",
      "hint": "숫자 1을 찾아보세요.",
      "answerOptions": [
        { "text": "One dollar", "isCorrect": true },
        { "text": "Five dollars", "isCorrect": false },
        { "text": "Ten dollars", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "숫자 '10'을 영어로 읽으면?",
      "hint : T로 시작하는 짧은 단어예요.",
      "answerOptions": [
        { "text": "Two", "isCorrect": false },
        { "text": "Ten", "isCorrect": true },
        { "text": "Twelve", "isCorrect": false }
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
      "id": "shiny_동전",
      "name": "반짝이는 동전",
      "description": "마트에서 받은 행운의 동전 아이템입니다."
    },
    {
      "type": "sticker",
      "id": "경제_doctor_badge_stage32",
      "name": "경제 박사 배지",
      "description": "\"가격을 잘 물어보는 똑똑한 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "Paying is easy when you know English! Let's go out now."
(영어를 알면 계산하는 것도 정말 쉬워! 이제 밖으로 나가자.)
