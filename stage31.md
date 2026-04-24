# Stage 31: 계산대 줄 서기 (Counting Items)

[상황 설명]
계산대 앞에 줄을 섰어요. 바구니에 담은 물건이 모두 몇 개인지 세어볼까요?

[Main Dialogue (대화)]
Buddy: "How many things do we have? Let's count."
(우리 물건이 몇 개나 있지? 세어보자.)

You: "**One** apple, **two** cookies, and **three** milks."
(사과 **하나**, 쿠키 **둘**, 그리고 우유 **셋**.)

Buddy: "Wait! I have **four** batteries and **five** candies, too!"
(잠깐! 나한테 배터리 **넷**이랑 사탕 **다섯** 개도 있어!)

You: "Wow, that is a lot! **One, two, three, four, five**..."
(와, 정말 많다! **하나, 둘, 셋, 넷, 다섯**...)

Buddy: "We are ready to pay now!"
(이제 계산할 준비가 됐어!)

[Stage 31 Quiz: 몇 개일까요?]
숫자를 영어로 세는 법을 복습해 봐요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "숫자 '3'을 영어로 하면?",
      "hint : T로 시작하고 r이 들어가는 단어예요.",
      "answerOptions": [
        { "text": "Two", "isCorrect": false },
        { "text": "Three", "isCorrect": true },
        { "text": "Five", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "숫자 '5'를 영어로 하면?",
      "hint : F로 시작하는 단어예요.",
      "answerOptions": [
        { "text": "Four", "isCorrect": false },
        { "text": "Five", "isCorrect": true },
        { "text": "Six", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "바구니에 사과가 하나 있을 때 하는 말은?",
      "hint": "하나를 뜻하는 숫자를 앞에 써요.",
      "answerOptions": [
        { "text": "One apple", "isCorrect": true },
        { "text": "Two apples", "isCorrect": false },
        { "text": "No apple", "isCorrect": false }
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
      "id": "숫자_주사위",
      "name": "숫자 주사위",
      "description": "1부터 6까지 숫자가 적힌 예쁜 주사위입니다."
    },
    {
      "type": "sticker",
      "id": "수학_천재_badge_stage31",
      "name": "수학 천재 배지",
      "description": "\"숫자를 잘 세는 똑똑한 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "You are good at counting! It's our turn now."
(너 숫자 정말 잘 세는구나! 이제 우리 차례야.)
