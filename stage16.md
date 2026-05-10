# Stage 16: 카드키 인식 (Push and Pull)

[상황 설명]
보안실 안으로 들어왔어요. 앞에 있는 기계를 작동시키려면 손잡이를 밀거나 당겨야 해요.

[Main Dialogue (대화)]
Buddy: "This machine is old. You need to **push** the button."
(이 기계는 오래됐어. 버튼을 **밀어야** 해.)

You: "Okay. I will **push** it. Oh, it's not working!"
(알았어. **밀어볼게**. 어, 안 되는데!)

Buddy: "Then try to **pull** the handle. **Pull** it hard! Use your **Number Code Table** to check if there are any other instructions!"
(그럼 손잡이를 **당겨봐**. 세게 **당겨!** 네 **숫자 암호표**를 확인해서 다른 지시사항이 있는지 봐봐!)

You: "I am **pulling**... Look! The lights are on! The **Rusty Key Card** really worked!"
(당기고 있어... 봐! 불이 들어왔어! **녹슨 카드키**가 정말 효과가 있었네!)

Buddy: "Great! **Push** for 'Yes', and **Pull** for 'No'."
(잘했어! '예'는 **밀고**, '아니오'는 **당겨**.)

[Stage 16 Quiz: 밀고 당기기!]
기계를 움직이기 위한 동작을 영어로 배워요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "물건을 앞으로 '밀다'라는 뜻의 단어는?",
      "hint : P로 시작하는 짧은 단어예요.",
      "answerOptions": [
        { "text": "Push", "isCorrect": true },
        { "text": "Pull", "isCorrect": false },
        { "text": "Jump", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "물건을 내 쪽으로 '당기다'라는 뜻의 단어는?",
      "hint : P로 시작하지만 L이 두 개 들어가요.",
      "answerOptions": [
        { "text": "Push", "isCorrect": false },
        { "text": "Pull", "isCorrect": true },
        { "text": "Walk", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "문 앞에 'PUSH'라고 써 있으면 어떻게 해야 할까요?",
      "hint": "미세요 라는 뜻이에요.",
      "answerOptions": [
        { "text": "당긴다", "isCorrect": false },
        { "text": "민다", "isCorrect": true },
        { "text": "가만히 있는다", "isCorrect": false }
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
      "id": "힘센_장갑",
      "name": "힘센 장갑",
      "description": "밀고 당기는 힘을 세게 해주는 장갑입니다."
    },
    {
      "type": "item",
      "id": "기계_조종사_면허증",
      "name": "기계 조종사 면허증",
      "description": "\"기계를 잘 다루는 친구\" 면허증입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"You are strong! The machine is working perfectly now.\""
    }
  ]
}
```