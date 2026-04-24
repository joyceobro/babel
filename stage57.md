# Stage 57: 기차 시간표 확인 (At the Station)

[상황 설명]
산업 구역용 기차역에 도착했어요. 기차와 버스가 어디로 가는지 확인해 봐요.

[Main Dialogue (대화)]
You: "Is this the **train station**?"
(여기가 **기차역**인가요?)

Buddy: "Yes, this is the **station**. Look at the big **train**!"
(응, 여기가 **역**이야. 저 커다란 **기차** 좀 봐!)

You: "I also see a **bus**. Where does it go?"
( **버스**도 보여. 저건 어디로 가니?)

Buddy: "The **bus** goes to the residential area. We need the **train**."
( **버스**는 거주 구역으로 가. 우린 **기차**를 타야 해.)

You: "Okay. Let's wait for the **train** at the **station**."
(알았어. **역**에서 **기차**를 기다리자.)

[Stage 57 Quiz: 어떤 걸 탈까요?]
교통수단과 관련된 장소의 이름을 영어로 골라보세요.

```json
{
  "questions": [
    {
      "questionNumber": 1,
      "question": "철길 위를 달리는 '기차'는 영어로?",
      "hint : T로 시작하는 단어예요. (Train)",
      "answerOptions": [
        { "text": "Train", "isCorrect": true },
        { "text": "Bus", "isCorrect": false },
        { "text": "Car", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 2,
      "question": "사람들이 많이 타는 커다란 '버스'는 영어로?",
      "hint : B로 시작하는 세 글자 단어예요.",
      "answerOptions": [
        { "text": "Train", "isCorrect": false },
        { "text": "Bus", "isCorrect": true },
        { "text": "Bike", "isCorrect": false }
      ]
    },
    {
      "questionNumber": 3,
      "question": "기차나 버스를 타는 '역'을 영어로 무엇이라고 하나요?",
      "hint : S로 시작하는 단어예요. (Station)",
      "answerOptions": [
        { "text": "Park", "isCorrect": false },
        { "text": "Station", "isCorrect": true },
        { "text": "School", "isCorrect": false }
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
      "id": "기차_모형",
      "name": "기차 모형",
      "description": "주머니에 쏙 들어가는 귀여운 기차 장난감입니다."
    },
    {
      "type": "sticker",
      "id": "베스트_승객_badge_stage57",
      "name": "베스트 승객 배지",
      "description": "\"대중교통을 잘 이용하는 친구\" 배지입니다."
    },
    {
      "type": "item",
      "id": "buddy",
      "name": "Buddy",
      "description": "\"The train is coming! Get ready to jump on.\""
    }
  ]
}
```