# Stage 14: 소음 추적 (Listen Carefully)

[상황 설명]
어디선가 이상한 소리가 들려요. "띠익- 띠익-" 소리를 따라가 봐야 해요.

[Main Dialogue (대화)]
Buddy: "**Listen!** Do you hear that?"
(들어봐! 저 소리 들리니?)

You: "Yes, I can hear a sound. It's very loud."
(응, 소리가 들려. 아주 커.)

Buddy: "**Listen carefully.** It's coming from that box."
(주의 깊게 **들어봐**. 저 상자에서 나는 소리야.)

You: "What is inside? Let's open it."
(안에 뭐가 들었을까? 열어보자.)

Buddy: "Wait! **Listen** again. It's a small bird robot! I think it can help us use our **Rusty Key Card** later."
(잠깐! 다시 **들어봐**. 작은 새 로봇이야! 저 친구가 나중에 우리 **녹슨 카드키**를 쓰는 걸 도와줄 수 있을 것 같아.)

[Stage 14 Quiz: 귀를 기울여요!]
소리를 들을 때 사용하는 표현을 익혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "소리에 귀를 기울이라고 할 때 쓰는 말은?",
      "hint : L로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Listen", "isCorrect": true },
        { "text": "Look", "isCorrect": false },
        { "text": "Eat", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "버디가 소리가 어디서 난다고 했나요?",
      "hint": "상자(box)를 찾아보세요.",
      "answerOptions": [
        { "text": "In the bag", "isCorrect": false },
        { "text": "From the box", "isCorrect": true },
        { "text": "On the tree", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "'Listen carefully.'에서 'carefully'의 뜻은?",
      "hint": "조심해서, 주의 깊게라는 뜻이에요.",
      "answerOptions": [
        { "text": "빨리", "isCorrect": false },
        { "text": "주의 깊게", "isCorrect": true },
        { "text": "시끄럽게", "isCorrect": false }
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
      "id": "황금_귀마개",
      "name": "황금 귀마개",
      "description": "작은 소리도 잘 들을 수 있게 해주는 귀마개입니다."
    },
    {
      "type": "item",
      "id": "소리_탐정_돋보기",
      "name": "소리 탐정 돋보기",
      "description": "소리의 근원지를 찾아주는 신기한 돋보기입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"You have great ears! The bird robot is safe now.\""
    }
  ]
}
```