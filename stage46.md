# Stage 46: 수리 로봇과 대화 (Fix and Wash)

[상황 설명]
작업장에서 열심히 일하고 있는 수리 로봇을 만났어요. 로봇들이 무슨 일을 하는지 물어봐요.

[Main Dialogue (대화)]
You: "What are you doing, robot?"
(로봇아, 뭐 하고 있니?)

Repair Robot: "I **fix** the broken gears. I am very busy."
(난 고장 난 톱니바퀴들을 **고쳐**. 아주 바쁘단다.)

Buddy: "Can I help you? I can **clean** the floor."
(내가 도와줄까? 난 바닥을 **청소할** 수 있어.)

You: "I can **wash** the dirty tools. Let's work together!"
(난 더러운 도구들을 **씻을** 수 있어. 같이 일하자!)

Repair Robot: "Thank you! **Fix**, **clean**, and **wash**... You are great helpers!"
(고마워! **고치고**, **청소하고**, **씻고**... 너희는 정말 좋은 조수들이구나!)

[Stage 46 Quiz: 어떤 일을 할까요?]
여러 가지 활동을 뜻하는 동사들을 익혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "고장 난 것을 '고치다'라는 뜻의 단어는?",
      "hint : F로 시작하는 세 글자 단어예요.",
      "answerOptions": [
        { "text": "Fix", "isCorrect": true },
        { "text": "Eat", "isCorrect": false },
        { "text": "Sleep", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "더러운 곳을 '청소하다'라는 뜻의 단어는?",
      "hint : C로 시작하는 단어예요. (Clean)",
      "answerOptions": [
        { "text": "Wash", "isCorrect": false },
        { "text": "Clean", "isCorrect": true },
        { "text": "Sing", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "물로 깨끗하게 '씻다'라는 뜻의 단어는?",
      "hint : W로 시작하는 단어예요. (Wash)",
      "answerOptions": [
        { "text": "Wash", "isCorrect": true },
        { "text": "Fix", "isCorrect": false },
        { "text": "Read", "isCorrect": false }
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
      "id": "비눗방울_총",
      "name": "비눗방울 총",
      "description": "청소할 때 쓰면 즐거운 비눗방울 총입니다."
    },
    {
      "type": "sticker",
      "id": "성실이_badge_stage46",
      "name": "성실이 배지",
      "description": "\"자기 일을 열심히 돕는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"Working together is easier! The workshop is clean now.\""
    }
  ]
}
```