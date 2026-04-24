# Stage 69: 실험 데이터 비교 (Fast and Slow)

[상황 설명]
두 로봇이 트랙 위에서 달리기 실험을 하고 있어요. 어느 로봇이 더 빠를까요?

[Main Dialogue (대화)]
Buddy: "Look at Robot A. It is very **fast**!"
(로봇 A를 봐. 정말 **빨라**!)

You: "Wow, it is so **fast**. But Robot B is very **slow**."
(와, 진짜 **빠르다**. 하지만 로봇 B는 아주 **느려**.)

Buddy: "Robot B is **slow**, but it is very careful."
(로봇 B는 **느리지만**, 아주 조심스럽단다.)

You: "I like the **fast** robot. It wins the race!"
(난 **빠른** 로봇이 좋아. 경주에서 이겼잖아!)

Buddy: "Sometimes **slow** is better than **fast**. Remember that!"
(가끔은 **느린** 것이 **빠른** 것보다 좋을 때가 있어. 기억해둬!)

[Stage 69 Quiz: 빨라요, 느려요?]
속도를 비교하는 반대말을 영어로 익혀보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "치타처럼 '빠르다'는 뜻의 영어 단어는?",
      "hint : F로 시작하는 단어예요. (Fast)",
      "answerOptions": [
        { "text": "Fast", "isCorrect": true },
        { "text": "Slow", "isCorrect": false },
        { "text": "Heavy", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "거북이처럼 '느리다'는 뜻의 영어 단어는?",
      "hint : S로 시작하는 단어예요. (Slow)",
      "answerOptions": [
        { "text": "Fast", "isCorrect": false },
        { "text": "Slow", "isCorrect": true },
        { "text": "Big", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "경주에서 이긴 로봇은 어떤 로봇이었나요?",
      "hint": "속도가 어떠했는지 생각해보세요.",
      "answerOptions": [
        { "text": "The slow robot", "isCorrect": false },
        { "text": "The fast robot", "isCorrect": true },
        { "text": "The small robot", "isCorrect": false }
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
      "id": "초고속_부스터",
      "name": "초고속 부스터",
      "description": "무엇이든 빠르게 만들어주는 마법의 장치입니다."
    },
    {
      "type": "sticker",
      "id": "거북이와_토끼_badge_stage69",
      "name": "거북이와 토끼 배지",
      "description": "\"속도보다 중요한 것을 아는 친구\" 배지입니다."
    }
  ]
}
```
Buddy: "The race is over. Now, let's go to the memory room."
(경주가 끝났어. 이제 기억의 방으로 가보자.)
