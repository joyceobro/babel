# Stage 55: 비밀 통로 방향 지시 (Left and Right)

[상황 설명]
비밀 통로로 들어왔어요. 갈림길이 나오는데, 어느 쪽으로 가야 할지 버디가 알려줘요.

[Main Dialogue (대화)]
Buddy: "Which way should we go? **Turn left** or **turn right**?"
(어느 길로 가야 할까? **왼쪽으로** 돌까, 아니면 **오른쪽으로** 돌까?)

You: "Wait, I see a secret mark. **Turn right**!"
(잠깐만, 비밀 표시가 보여. **오른쪽으로 돌아**!)

Buddy: "Okay, **turn right**. Now, there is another turn. **Turn left**!"
(알았어, **오른쪽으로 돌자**. 이제 또 꺾이는 곳이야. **왼쪽으로 돌아**!)

You: "Right, then left. We are almost there!"
(오른쪽, 그다음에 왼쪽. 거의 다 왔어!)

Buddy: "You are a great navigator. **Right** and **left**... you know them all!"
(넌 정말 훌륭한 항해사야. **오른쪽**이랑 **왼쪽**... 다 알고 있구나!)

[Stage 55 Quiz: 왼쪽? 오른쪽?]
방향을 나타내는 기초 표현을 다시 한번 확인해 봐요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "'왼쪽으로 도세요'라는 뜻의 영어 표현은?",
      "hint : L로 시작하는 단어를 써요. (Left)",
      "answerOptions": [
        { "text": "Turn left", "isCorrect": true },
        { "text": "Turn right", "isCorrect": false },
        { "text": "Go straight", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "'오른쪽으로 도세요'라는 뜻의 영어 표현은?",
      "hint : R로 시작하는 단어를 써요. (Right)",
      "answerOptions": [
        { "text": "Turn left", "isCorrect": false },
        { "text": "Turn right", "isCorrect": true },
        { "text": "Stop here", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "첫 번째 갈림길에서 우리가 선택한 방향은?",
      "hint": "대화를 다시 읽어보세요. (Right!)",
      "answerOptions": [
        { "text": "Left", "isCorrect": false },
        { "text": "Right", "isCorrect": true },
        { "text": "Up", "isCorrect": false }
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
      "id": "방향_지시등",
      "name": "방향 지시등",
      "description": "왼쪽과 오른쪽을 알려주는 반짝이는 지시등입니다."
    },
    {
      "type": "sticker",
      "id": "길잡이_badge_stage55",
      "name": "길잡이 배지",
      "description": "\"복잡한 길도 잘 찾는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"We found the exit! Your direction skills are amazing.\""
    }
  ]
}
```