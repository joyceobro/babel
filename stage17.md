# Stage 17: 비상구로 달리기 (Run, Jump, Walk)

[상황 설명]
경보음이 울려요! 경비 로봇들이 오고 있어요. 빨리 비상구를 향해 달려야 해요!

[Main Dialogue (대화)]
Buddy: "Hurry! **Run** to the exit!"
(서둘러! 출구까지 **달려!**)

You: "I am **running**! But there is a hole in the floor!"
(달리고 있어! 하지만 바닥에 구멍이 있어!)

Buddy: "**Jump** over it! **Jump** high!"
(그 위로 **점프해**! 높이 **뛰어!**)

You: "Whew, I did it. Now what?"
(휴, 해냈어. 이제 어떡해?)

Buddy: "Now **walk** quietly. The guards are near."
(이제 조용히 **걸어**. 경비들이 가까이 있어.)

[Stage 17 Quiz: 어떻게 움직일까요?]
몸을 움직이는 여러 가지 동작을 영어로 골라보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "빨리 '달리다'라는 뜻의 단어는?",
      "hint": "R로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Run", "isCorrect": true },
        { "text": "Walk", "isCorrect": false },
        { "text": "Sit", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "위로 '폴짝 뛰다'라는 뜻의 단어는?",
      "hint": "J로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Jump", "isCorrect": true },
        { "text": "Run", "isCorrect": false },
        { "text": "Sleep", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "천천히 '걷다'라는 뜻의 단어는?",
      "hint": "W로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Walk", "isCorrect": true },
        { "text": "Run", "isCorrect": false },
        { "text": "Jump", "isCorrect": false }
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
      "id": "날쌘돌이_신발",
      "name": "날쌘돌이 신발",
      "description": "더 빨리 달릴 수 있게 해주는 신발입니다."
    },
    {
      "type": "sticker",
      "id": "운동_선수_badge_stage17",
      "name": "운동 선수 뱃지",
      "description": "\"몸놀림이 가벼운 친구\" 뱃지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"You are very fast! We escaped the guards. Great job!\""
    }
  ]
}
```