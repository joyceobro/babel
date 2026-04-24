# Stage 26: 상점가 구경 (What is This?)

[상황 설명]
가게들이 아주 많은 상점가에 왔어요. 신기한 물건들이 아주 많네요!

[Main Dialogue (대화)]
You: "Buddy, **what is this**? It is very shiny."
(버디야, **이건 뭐야**? 아주 반짝거려.)

Buddy: "Oh, **this is** a robot watch. It tells the time."
(아, **이건** 로봇 시계야. 시간을 알려주지.)

You: "And **what is that** over there? On the high shelf?"
(그럼 저기 위에 있는 **저건 뭐야**? 높은 선반 위에 있는 거 말이야.)

Buddy: "**That is** a magic hat. It changes colors!"
( **저건** 마법 모자야. 색깔이 변한단다!)

You: "Wow! **This is** cool, and **that is** amazing!"
(와! **이건** 멋지고, **저건** 놀랍다!)

[Stage 26 Quiz: 이게 뭐예요?]
가까운 물건과 먼 물건을 묻고 답하는 법을 배워요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "가까이 있는 물건을 가리키며 '이건 뭐야?'라고 물을 때?",
      "hint": "What is ____? 빈칸에 들어갈 가까운 것을 뜻하는 말은?",
      "answerOptions": [
        { "text": "this", "isCorrect": true },
        { "text": "that", "isCorrect": false },
        { "text": "it", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "멀리 있는 물건을 가리키며 '저건 뭐야?'라고 물을 때?",
      "hint": "What is ____? 빈칸에 들어갈 먼 것을 뜻하는 말은?",
      "answerOptions": [
        { "text": "this", "isCorrect": false },
        { "text": "that", "isCorrect": true },
        { "text": "me", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "상자 안에 있는 '이것'을 설명할 때 알맞은 문장은?",
      "hint": "This is... 로 시작해보세요.",
      "answerOptions": [
        { "text": "This is a book", "isCorrect": true },
        { "text": "That is a star", "isCorrect": false },
        { "text": "I like bread", "isCorrect": false }
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
      "id": "shiny_시계",
      "name": "반짝이는 시계",
      "description": "시간을 알려주는 멋진 로봇 시계입니다."
    },
    {
      "type": "sticker",
      "id": "물음표_badge_stage26",
      "name": "물음표 배지",
      "description": "\"호기심이 많은 똑똑한 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "There are so many things to see. Let's look at more shops!"
(볼거리가 정말 많아. 다른 가게들도 더 둘러보자!)
