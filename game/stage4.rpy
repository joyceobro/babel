# Stage 4: 신호등 게임 (Open and Close)

label stage_4:
    scene stage4_bg with fade
    
    "커다란 철문 앞에 도착했어요. 이 문은 특이하게도 '열려라!'와 '닫혀라!'라는 말을 알아들어야 열린대요."
    
    show buddy_lovely_happy at center with dissolve
    
    b "This door is a bit funny. It only opens when you say the right word."
    
    p "What should I say?"
    
    b "The door is closed now. Say 'Open!'"
    
    p "Open! Look, it is moving!"
    
    b "Great! Now, if a bad robot comes, say 'Close!' very fast."

    jump stage_4_quiz

label stage_4_quiz:
    b "Choose the right word for the door!"

    # Question 1
    label s4_q1:
        b "The door is closed. What do you say to open it?"
        menu:
            "Open":
                b "Yes! The door opens."
            "Close":
                b "No, it's already closed! Try again."
                $ wrong_answer()
                jump s4_q1
            "Hello":
                b "The door doesn't care about greetings! Try again."
                $ wrong_answer()
                jump s4_q1

    # Question 2
    label s4_q2:
        b "What if you want to close the door?"
        menu:
            "Open":
                b "No, that opens it! Try again."
                $ wrong_answer()
                jump s4_q2
            "Close":
                b "Correct! It shuts tight."
            "Sit":
                b "The door cannot sit! Try again."
                $ wrong_answer()
                jump s4_q2

    # Question 3
    label s4_q3:
        b "What does 'fast' mean in 'Say Close very fast'?"
        menu:
            "느리게":
                b "No, that's 'slowly'. Try again."
                $ wrong_answer()
                jump s4_q3
            "조용히":
                b "No, that's 'quietly'. Try again."
                $ wrong_answer()
                jump s4_q3
            "빠르게":
                b "Yes! Speed is important."

    # Reward and ending of stage 4
    b "You are getting better at this! Let's go through the door."
    
    $ add_reward(reward_type="item", id="마법의_열쇠고리", name="마법의 열쇠고리", description="문을 더 쉽게 열 수 있게 도와주는 행운의 열쇠고리입니다.")
    $ add_reward(reward_type="sticker", id="문지기_sticker_stage4", name="문지기 스티커", description="\"문을 잘 여는 친구\" 스티커를 받았습니다.")

    b "Stay sharp!"
    
    return
