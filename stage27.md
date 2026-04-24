# Stage 27: 빵집에서 빵 고르기 (At the Bakery)

[상황 설명]
고소한 냄새를 따라 빵집에 들어왔어요. 맛있어 보이는 빵과 과자들이 정말 많아요!

[Main Dialogue (대화)]
Baker Robot: "Welcome! We have many delicious things."
(어서 오세요! 맛있는 것들이 아주 많답니다.)

You: "I want to buy some **bread**. And maybe a **cookie**."
( **빵**을 좀 사고 싶어요. 그리고 **쿠키**도요.)

Buddy: "Look at that big **cake**! It has many strawberries."
(저 커다란 **케이크** 좀 봐! 딸기가 아주 많이 올라가 있어.)

You: "I like **cookies** more than **cake**. Can I have three **cookies**?"
(난 **케이크**보다 **쿠키**가 더 좋아. **쿠키** 세 개만 주실래요?)

Baker Robot: "Sure! Here is your **bread** and **cookies**."
(물론이죠! 여기 **빵**과 **쿠키**입니다.)

[Stage 27 Quiz: 맛있는 간식!]
빵집에 있는 음식들의 이름을 영어로 맞춰보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "매일 먹어도 맛있는 '빵'을 영어로 하면?",
      "hint : B로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Bread", "isCorrect": true },
        { "text": "Water", "isCorrect": false },
        { "text": "Candy", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "생일 파티에 빠질 수 없는 '케이크'는 영어로?",
      "hint : C로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Bread", "isCorrect": false },
        { "text": "Cake", "isCorrect": true },
        { "text": "Cookie", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "바삭바삭하고 달콤한 '쿠키'는 영어로?",
      "hint : C로 시작하고 뒤에 ie가 붙어요.",
      "answerOptions": [
        { "text": "Cookie", "isCorrect": true },
        { "text": "Juice", "isCorrect": false },
        { "text": "Milk", "isCorrect": false }
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
      "id": "초코_쿠키",
      "name": "초코 쿠키",
      "description": "달콤한 냄새가 나는 초코 쿠키 아이템입니다."
    },
    {
      "type": "sticker",
      "id": "꼬마_파티쉐_badge_stage27",
      "name": "꼬마 파티쉐 배지",
      "description": "\"빵을 좋아하는 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "The cookies look so good! Let's share them later."
(쿠키 정말 맛있어 보인다! 나중에 같이 나눠 먹자.)
