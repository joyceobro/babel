# Stage 13: 청소기 돕기 (Help Me, Please)

[상황 설명]
작은 로봇 청소기가 구석에 끼어서 옴짝달싹 못 하고 있어요. 우리에게 도움을 요청하네요!

[Main Dialogue (대화)]
Cleaner Robot: "**Help me, please!** I am stuck!"
(제발 **도와주세요!** 몸이 끼었어요!)

You: "Oh no! Buddy, let's help him."
(안돼! 버디야, 우리가 도와주자.)

Buddy: "Okay! Pull the robot, please."
(좋아! 로봇을 당겨줘.)

You: "One, two, three! I did it!"
(하나, 둘, 셋! 해냈어!)

Cleaner Robot: "Thank you! You are so kind. **Help me** find my way back, too."
(고마워요! 정말 친절하시네요. 제가 돌아가는 길도 **도와주세요**.)

[Stage 13 Quiz: 도와주세요!]
도움을 주고받을 때 사용하는 정중한 표현을 골라보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "도움이 필요할 때 가장 많이 쓰는 말은?",
      "hint": "H로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Help me!", "isCorrect": true },
        { "text": "Stop me!", "isCorrect": false },
        { "text": "Follow me!", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "부탁을 할 때 뒤에 붙이면 더 예의 바른 말은?",
      "hint : P로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Sorry", "isCorrect": false },
        { "text": "Please", "isCorrect": true },
        { "text": "Hello", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "로봇이 왜 'Help me'라고 했나요?",
      "hint": "Stuck의 의미를 생각해보세요.",
      "answerOptions": [
        { "text": "배가 고파서", "isCorrect": false },
        { "text": "몸이 끼어서", "isCorrect": true },
        { "text": "졸려서", "isCorrect": false }
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
      "id": "shiny_빗자루",
      "name": "반짝이는 빗자루",
      "description": "청소를 도와주는 신기한 빗자루입니다."
    },
    {
      "type": "sticker",
      "id": "친절_대사_badge_stage13",
      "name": "친절 대사 배지",
      "description": "남을 돕는 착한 친구에게 주는 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"Helping others makes me feel good. You are a true hero!\""
    }
  ]
}
```