# Stage 52: 물건 옮기기 (Heavy and Light)

[상황 설명]
부품 상자들을 옮겨야 해요. 어떤 상자는 아주 무겁고, 어떤 상자는 아주 가벼워요.

[Main Dialogue (대화)]
You: "Ugh! This big box is very **heavy**. I can't lift it."
(으악! 이 커다란 상자는 너무 **무거워**. 들 수가 없어.)

Buddy: "Let me help you. This small box is **light**."
(내가 도와줄게. 이 작은 상자는 **가벼워**.)

You: "Wow, it really is **light**. I can carry two!"
(와, 정말 **가볍네**. 두 개도 들 수 있겠어!)

Buddy: "Be careful with the **heavy** box. Use the robot cart."
( **무거운** 상자는 조심해. 로봇 카트를 이용하자.)

You: "Okay. **Heavy** boxes go on the cart, and I will carry the **light** ones."
(알았어. **무거운** 상자는 카트에 싣고, 난 **가벼운** 걸 들게.)

[Stage 52 Quiz: 무거운가요, 가벼운가요?]
무게를 비교하는 형용사를 배워보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "코끼리처럼 '무겁다'는 뜻의 영어 단어는?",
      "hint : H로 시작하는 단어예요. (Heavy)",
      "answerOptions": [
        { "text": "Heavy", "isCorrect": true },
        { "text": "Light", "isCorrect": false },
        { "text": "Small", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "깃털처럼 '가볍다'는 뜻의 영어 단어는?",
      "hint : L로 시작하는 단어예요. (Light)",
      "answerOptions": [
        { "text": "Heavy", "isCorrect": false },
        { "text": "Light", "isCorrect": true },
        { "text": "Fast", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "무거운 상자를 옮길 때 무엇을 사용했나요?",
      "hint": "바퀴가 달린 물건이에요.",
      "answerOptions": [
        { "text": "Cart", "isCorrect": true },
        { "text": "Ball", "isCorrect": false },
        { "text": "Cake", "isCorrect": false }
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
      "id": "튼튼한_장갑",
      "name": "튼튼한 장갑",
      "description": "무거운 물건도 잘 들 수 있게 해주는 마법 장갑입니다."
    },
    {
      "type": "sticker",
      "id": "힘센_친구_badge_stage52",
      "name": "힘센 친구 배지",
      "description": "\"어려운 일도 척척 돕는 힘센 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"We finished moving all the boxes! You are stronger than you look.\""
    }
  ]
}
```