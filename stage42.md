# Stage 42: 작업장 위치 (Top, Bottom, Middle)

[상황 설명]
커다란 선반 위에 부품들이 쌓여 있어요. 버디가 필요한 부품이 어디에 있는지 알려주네요.

[Main Dialogue (대화)]
Buddy: "We need the red gear. It is on the **top** shelf."
(우린 빨간 톱니바퀴가 필요해. **맨 위쪽** 선반에 있어.)

You: "I see it! What about the blue tool? Is it at the **bottom**?"
(찾았다! 파란 공구는 어때? **맨 아래쪽**에 있니?)

Buddy: "No, the blue tool is in the **middle**."
(아니, 파란 공구는 **중간**에 있어.)

You: "Okay. Red is at the **top**, blue is in the **middle**, and yellow is at the **bottom**!"
(알았어. 빨간 건 **맨 위**, 파란 건 **중간**, 그리고 노란 건 **맨 아래**!)

Buddy: "You are right! Now let's pick them up."
(정답이야! 이제 그것들을 집어 들자.)

[Stage 42 Quiz: 어디에 있나요?]
위치를 나타내는 세 가지 핵심 표현을 익혀봐요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "'맨 위'를 뜻하는 영어 단어는?",
      "hint : T로 시작하는 세 글자 단어예요.",
      "answerOptions": [
        { "text": "Top", "isCorrect": true },
        { "text": "Middle", "isCorrect": false },
        { "text": "Bottom", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "'맨 아래'를 뜻하는 영어 단어는?",
      "hint : B로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Top", "isCorrect": false },
        { "text": "Middle", "isCorrect": false },
        { "text": "Bottom", "isCorrect": true }
      ]
    },
    {
      "questionNumber": 3,
      "question": "'중간'을 뜻하는 영어 단어는?",
      "hint : M으로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Top", "isCorrect": false },
        { "text": "Middle", "isCorrect": true },
        { "text": "Bottom", "isCorrect": false }
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
      "id": "마법의_집게",
      "name": "마법의 집게",
      "description": "높은 곳에 있는 물건도 쉽게 집을 수 있는 집게입니다."
    },
    {
      "type": "sticker",
      "id": "정리_정돈_badge_stage42",
      "name": "정리 정돈 배지",
      "description": "\"물건의 위치를 잘 기억하는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"You have a great memory! We found all the parts.\""
    }
  ]
}
```