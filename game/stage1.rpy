# Stage 1: 깨어난 방 (The Magic Room)

label stage_1:
    play music "audio/stage1_ambient.ogg" loop fadein 2.0

    "깜깜한 방, 침대에서 눈을 떴어요. 머리가 조금 어질어질해요."
    "그때, 귀여운 꼬마 로봇 '버디'가 눈을 반짝이며 다가와요."
    
    show buddy_lovely_happy at center with dissolve 
    
    b "Hello! Can you hear me? Wake up!"
    
    p "Oh... Who are you?"
    
    b "I am Buddy. I am a helper robot. Don't be afraid!"
    
    p "Where am I? It's so dark here."
    
    b "You are in a big tower. People cannot speak English now. But you can! That is cool!"
    
    p "I want to go home."
    
    b "I can help you. Let's go together. Follow me!"

    "문을 열고 나가려면 버디의 질문에 알맞은 답을 해야 해요. 화면의 버튼을 눌러보세요!"

    jump stage_1_quiz

label stage_1_quiz:
    b "First mission! Answer my questions to open the door."

    # Question 1
    label s1_q1:
        b "What does 'Don't be afraid!' mean?"
        menu:
            "배고프지 마!":
                b "No, that's not it. Try again!"
                $ wrong_answer()
                jump s1_q1
            "무서워하지 마!":
                b "Correct! You are doing great."
            "졸지 마!":
                b "No, that's not it. Try again!"
                $ wrong_answer()
                jump s1_q1

    # Question 2
    label s1_q2:
        b "What kind of robot am I?"
        menu:
            "요리하는 로봇":
                b "No, I can't cook yet! Try again."
                $ wrong_answer()
                jump s1_q2
            "싸우는 로봇":
                b "No, I am peaceful! Try again."
                $ wrong_answer()
                jump s1_q2
            "도와주는 로봇":
                b "Yes! I am a helper robot."

    # Question 3
    label s1_q3:
        b "What did I say when I asked you to follow me?"
        menu:
            "Follow me!":
                b "That's right! Let's go!"
            "Sit down!":
                b "No, we need to move! Try again."
                $ wrong_answer()
                jump s1_q3
            "Good bye!":
                b "Not yet! We just met. Try again."
                $ wrong_answer()
                jump s1_q3

    # Reward and ending of stage 1
    b "Good job! You are very smart."
    
    $ add_reward(reward_type="item", id="buddy_candy", name="버디의 사탕", description="버디가 기운을 내라며 반짝이는 사탕 아이템을 줍니다.", icon="gui/bubble.png", effect={"energy": 1})
    $ add_reward(reward_type="sticker", id="praise_sticker_stage1", name="칭찬 스티커", description="\"영어 천재의 탄생!\" 스티커가 다이어리에 붙습니다.", icon="gui/namebox.png")

    b "Now, walk quietly. There is a scary guard robot outside!"
    
    return
