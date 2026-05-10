# Stage 5: 카메라 피하기 (Hide and Seek)

[상황 설명]
천장에 빨간 눈을 가진 감시 카메라가 돌아가고 있어요! 버디가 다급하게 당신을 불러요.

[Main Dialogue (대화)]
Buddy: "Wait! A guard robot is coming. Hide **behind** that big box!"
(잠깐! 경비 로봇이 오고 있어. 저 커다란 상자 **뒤에** 숨어!)

You: "Okay! What about you, Buddy?"
(알았어! 버디 너는?)

Buddy: "I'll stay **next to** the pillar. Stay quiet! Use your **soft shoes** to walk silently!"
(나는 기둥 **옆에** 있을게. 조용히 해! 네 **부드러운 신발**을 신어서 소리 내지 말고 걸어!)

You: "I am scared. The camera is looking at the box."
(무서워. 카메라가 상자를 보고 있어.)

Buddy: "Don't move. You are safe **behind** the box."
(움직이지 마. 상자 **뒤에** 있으면 안전해.)

[Stage 5 Quiz: 어디에 숨었나요?]
버디와 당신의 위치를 정확히 알고 있나요?

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "상자 '뒤에' 숨으라고 할 때 사용한 단어는?",
      "hint": "물건의 뒷면을 뜻하는 전치사예요.",
      "answerOptions": [
        { "text": "Behind", "isCorrect": true },
        { "text": "Next to", "isCorrect": false },
        { "text": "On", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "버디는 기둥 '옆에' 있겠다고 했어요. '옆에'는 영어로?",
      "hint": "가까운 옆자리를 말할 때 써요.",
      "answerOptions": [
        { "text": "Behind", "isCorrect": false },
        { "text": "Next to", "isCorrect": true },
        { "text": "Under", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "버디가 왜 숨으라고 했나요?",
      "hint": "상황 설명을 다시 읽어보세요.",
      "answerOptions": [
        { "text": "잠을 자기 위해서", "isCorrect": false },
        { "text": "경비 로봇을 피하려고", "isCorrect": true },
        { "text": "숨바꼭질 놀이를 하려고", "isCorrect": false }
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
      "id": "투명_망토_조각",
      "name": "투명 망토 조각",
      "description": "몸을 살짝 가려주는 신비한 천 조각입니다."
    },
    {
      "type": "sticker",
      "id": "닌자_badge_stage5",
      "name": "닌자 배지",
      "description": "\"은신술의 달인\" 배지를 획득했습니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"The guard is gone. Good job! You stayed very quiet.\""
    }
  ]
}
```