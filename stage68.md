# Stage 68: 날씨 기록하기 (Sunny and Rainy)

[상황 설명]
실험실 창문을 통해 바깥 날씨를 확인하고 기록해야 해요. 오늘 날씨는 어떤가요?

[Main Dialogue (대화)]
Buddy: "How is the weather today? Is it **sunny**?"
(오늘 날씨가 어떠니? **화창하니**?)

You: "No, it is not **sunny**. It is **rainy** now."
(아니, **화창하지** 않아. 지금은 **비가 와**.)

Buddy: "Look! The clouds are moving. It is getting **cloudy**."
(봐! 구름이 움직여. **흐려지고** 있어.)

You: "I hope it becomes **sunny** soon. I don't like **rainy** days."
(곧 **화창해지면** 좋겠다. 난 **비 오는** 날이 싫어.)

Buddy: "**Sunny**, **rainy**, or **cloudy**... the weather is always interesting!"
( **화창하든**, **비가 오든**, **흐리든**... 날씨는 항상 흥미로워!)

[Stage 68 Quiz: 오늘 날씨는 어때요?]
날씨를 나타내는 여러 가지 표현을 익혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "해가 쨍쨍한 '화창한' 날씨는 영어로?",
      "hint : Sun 뒤에 ny를 붙여요.",
      "answerOptions": [
        { "text": "Sunny", "isCorrect": true },
        { "text": "Rainy", "isCorrect": false },
        { "text": "Snowy", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "비가 내리는 '비 오는' 날씨는 영어로?",
      "hint : Rain 뒤에 y를 붙여요.",
      "answerOptions": [
        { "text": "Sunny", "isCorrect": false },
        { "text": "Rainy", "isCorrect": true },
        { "text": "Cloudy", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "구름이 많이 낀 '흐린' 날씨는 영어로?",
      "hint : Cloud 뒤에 y를 붙여요.",
      "answerOptions": [
        { "text": "Cloudy", "isCorrect": true },
        { "text": "Windy", "isCorrect": false },
        { "text": "Hot", "isCorrect": false }
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
      "id": "날씨_달력",
      "name": "날씨 달력",
      "description": "매일매일 날씨를 스티커로 표시할 수 있는 달력입니다."
    },
    {
      "type": "sticker",
      "id": "기상_캐스터_badge_stage68",
      "name": "기상 캐스터 배지",
      "description": "\"날씨를 잘 관찰하고 기록하는 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "The weather is changing again! Let's finish our work."
(날씨가 또 변하고 있어! 우리 일을 마무리하자.)
