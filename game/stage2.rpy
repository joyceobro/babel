# Stage 2: 어두운 복도 (The Dark Hallway)

label stage_2:
    scene stage2_bg with fade
    
    "버디를 따라 방 밖으로 나왔어요. 복도는 아주 길고 어두워요."
    "버디가 당신의 얼굴을 살피며 물어봐요."
    
    show buddy_lovely_happy at center with dissolve
    
    b "How are you? Are you okay?"
    
    p "I am a little scared. It is very dark."
    
    b "I am happy because I am with you! Look, I have a small light."
    
    p "That is good. I am hungry, too."
    
    b "Don't worry. We can find some bread soon! Oh, wait! Do you have the Buddy Candy? It can give you energy!"

    jump stage_2_quiz

label stage_2_quiz:
    b "Tell me how you feel!"

    # Question 1
    label s2_q1:
        b "How are you?"
        menu:
            "I am fine, thank you.":
                b "That's good to hear!"
            "I am a robot.":
                b "No, you are a human! Try again."
                $ wrong_answer()
                jump s2_q1
            "Hello, Buddy.":
                b "Hello, but I asked how you are! Try again."
                $ wrong_answer()
                jump s2_q1

    # Question 2
    label s2_q2:
        b "What does 'I am hungry' mean?"
        menu:
            "졸려요.":
                b "No, that's 'I am sleepy'. Try again."
                $ wrong_answer()
                jump s2_q2
            "배고파요.":
                b "Correct! We need food."
            "심심해요.":
                b "No, that's 'I am bored'. Try again."
                $ wrong_answer()
                jump s2_q2

    # Question 3
    label s2_q3:
        b "Why did I say 'I am happy'?"
        menu:
            "함께 있어서":
                b "Yes! I am happy because we are together."
            "혼자 있어서":
                b "No, I like being with friends! Try again."
                $ wrong_answer()
                jump s2_q3
            "잠을 자서":
                b "No, that's not it. Try again."
                $ wrong_answer()
                jump s2_q3

    # Reward and ending of stage 2
    b "You are doing great! Let's keep going."
    
    $ add_reward(reward_type="item", id="small_flashlight", name="작은 손전등", description="어두운 곳을 밝힐 수 있는 귀여운 손전등입니다.")
    $ add_reward(reward_type="sticker", id="courage_badge_stage2", name="용기의 뱃지", description="\"무서움을 이겨내자!\" 뱃지를 획득했습니다.")

    b "Shhh, I hear a robot moving!"
    
    return
