# Stage 1: 깨어난 방 (The Magic Room)

[상황 설명]
깜깜한 방, 침대에서 눈을 떴어요. 머리가 조금 어질어질해요. 그때, 귀여운 꼬마 로봇 **'버디'**가 눈을 반짝이며 다가와요.

[Main Dialogue (대화)]
Buddy: "Hello! Can you hear me? Wake up!"
(안녕! 내 목소리 들려? 일어나 봐!)

You: "Oh... Who are you?"
(어... 너는 누구니?)

Buddy: "I am Buddy. I am a helper robot. Don't be afraid!"
(나는 버디야. 도우미 로봇이지. 무서워하지 마!)

You: "Where am I? It's so dark here."
(여긴 어디야? 너무 어두워.)

Buddy: "You are in a big tower. People cannot speak English now. But you can! That is cool!"
(너는 커다란 탑에 있어. 지금 사람들은 영어를 못 해. 하지만 너는 할 줄 알잖아! 정말 멋져!)

You: "I want to go home."
(집에 가고 싶어.)

Buddy: "I can help you. Let's go together. Follow me!"
(내가 도와줄게. 같이 가자. 나를 따라와!)

[Stage 1 Quiz: 첫 번째 미션!]
문을 열고 나가려면 버디의 질문에 알맞은 답을 해야 해요. 화면의 버튼을 눌러보세요!

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "버디가 'Don't be afraid!'라고 말했어요. 무슨 뜻일까요?",
      "hint": "새로운 친구를 만났을 때 안심시켜주는 말이에요.",
      "answerOptions": [
        { "text": "배고프지 마!", "isCorrect": false },
        { "text": "무서워하지 마!", "isCorrect": true },
        { "text": "졸지 마!", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "버디는 어떤 로봇인가요?",
      "hint": "Buddy: 'I am a helper robot.'",
      "answerOptions": [
        { "text": "요리하는 로봇", "isCorrect": false },
        { "text": "싸우는 로봇", "isCorrect": false },
        { "text": "도와주는 로봇", "isCorrect": true }
      ]
    },
    {
      "questionNumber": 3,
      "question": "밖으로 나가고 싶을 때 버디가 한 말은?",
      "hint": "나를 따라오라고 할 때 쓰는 말이에요.",
      "answerOptions": [
        { "text": "Follow me!", "isCorrect": true },
        { "text": "Sit down!", "isCorrect": false },
        { "text": "Good bye!", "isCorrect": false }
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
      "id": "buddy_candy",
      "name": "버디의 사탕",
      "description": "버디가 기운을 내라며 반짝이는 사탕 아이템을 줍니다.",
      "effect": {
        "energy": 1
      }
    },
    {
      "type": "sticker",
      "id": "praise_sticker_stage1",
      "name": "칭찬 스티커",
      "description": "\"영어 천재의 탄생!\" 스티커가 다이어리에 붙습니다."
    }
  ]
}
```

Buddy: "Good job! You are very smart. Now, walk quietly. There is a scary guard robot outside!"
(잘했어! 넌 정말 똑똑하구나. 이제 조용히 걸어줘. 밖에 무서운 경비 로봇이 있거든!)
