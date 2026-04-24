# Stage 62: 책 제목 찾기 (Books and Stories)

[상황 설명]
책장에서 우리가 찾는 책을 골라야 해요. 책과 관련된 단어들을 배워볼까요?

[Main Dialogue (대화)]
Buddy: "Look at this **book**. The **title** is 'Babel's Secret'."
(이 **책** 좀 봐. **제목**이 '바벨의 비밀'이야.)

You: "Is it a long **story**? I want to read it."
(긴 **이야기**니? 읽어보고 싶어.)

Buddy: "It has many **pages**. Let's look at **page** ten."
( **페이지**가 아주 많아. 10 **쪽**을 보자.)

You: "This **story** is very interesting! Can I turn the **page**?"
(이 **이야기** 정말 흥미로워! **페이지**를 넘겨도 될까?)

Buddy: "Sure. Read the **book** carefully."
(그럼. **책**을 주의 깊게 읽어봐.)

[Stage 62 Quiz: 책 속의 세상!]
책과 관련된 명칭을 영어로 맞춰보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "우리가 읽는 '책'을 영어로 하면?",
      "hint : B로 시작하는 단어예요. (Book)",
      "answerOptions": [
        { "text": "Book", "isCorrect": true },
        { "text": "Pen", "isCorrect": false },
        { "text": "Desk", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "책 안의 한 장 한 장을 뜻하는 '쪽' 혹은 '페이지'는?",
      "hint : P로 시작하는 단어예요. (Page)",
      "answerOptions": [
        { "text": "Paper", "isCorrect": false },
        { "text": "Page", "isCorrect": true },
        { "text": "Title", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "책이 들려주는 재미있는 '이야기'는 영어로?",
      "hint : S로 시작하는 단어예요. (Story)",
      "answerOptions": [
        { "text": "Song", "isCorrect": false },
        { "text": "Story", "isCorrect": true },
        { "text": "Game", "isCorrect": false }
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
      "id": "shiny_책갈피",
      "name": "반짝이는 책갈피",
      "description": "읽던 곳을 표시해주는 예쁜 책갈피입니다."
    },
    {
      "type": "sticker",
      "id": "독서왕_badge_stage62",
      "name": "독서왕 배지",
      "description": "\"책 읽기를 좋아하는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"Books are like magic! They tell us everything.\""
    }
  ]
}
```