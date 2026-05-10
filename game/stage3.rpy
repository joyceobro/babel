# Stage 3: 멈춰선 로봇 (The Sleeping Robot)

label stage_3:
    scene stage3_bg with fade
    
    "복도 한가운데에 커다란 로봇이 길을 막고 서 있어요."
    "복도가 어두워서 잘 안 보이지만, 작은 손전등을 비춰보니 눈에 불이 꺼져 있는 걸 보니 잠시 멈춰 있는 것 같아요."
    
    show buddy_lovely_happy at center with dissolve
    
    b "Wait! A robot is sleeping. We must be very quiet."
    
    p "Should I stop?"
    
    b "Yes, stop! Don't move. If it wakes up, say 'Sit down!'"
    
    p "Okay. What if it comes closer?"
    
    b "Then say 'Stand!' and then 'Stop!'. It's a simple command."

    jump stage_3_quiz

label stage_3_quiz:
    b "Try to command the robot!"

    # Question 1
    label s3_q1:
        b "How do you make a moving robot stop?"
        menu:
            "Run!":
                b "No, that's the opposite! Try again."
                $ wrong_answer()
                jump s3_q1
            "Stop!":
                b "Correct! It stops moving."
            "Go!":
                b "No, it will keep going! Try again."
                $ wrong_answer()
                jump s3_q1

    # Question 2
    label s3_q2:
        b "How do you tell the robot to 'Sit down'?"
        menu:
            "Sit down!":
                b "Yes! Good command."
            "Stand up!":
                b "No, that makes it stand! Try again."
                $ wrong_answer()
                jump s3_q2
            "Jump!":
                b "No, we don't want it to jump! Try again."
                $ wrong_answer()
                jump s3_q2

    # Question 3
    label s3_q3:
        b "What does 'Don't move' mean?"
        menu:
            "움직이지 마.":
                b "That's right! Stay still."
            "노래하지 마.":
                b "No, that's 'Don't sing'. Try again."
                $ wrong_answer()
                jump s3_q3
            "뛰지 마.":
                b "No, that's 'Don't run'. Try again."
                $ wrong_answer()
                jump s3_q3

    # Reward and ending of stage 3
    b "Whew, it didn't wake up! You are a natural leader."
    
    $ add_reward(reward_type="item", id="정지_리모컨", name="정지 리모컨", description="로봇들을 잠시 멈추게 할 수 있는 신기한 리모컨입니다.")
    $ add_reward(reward_type="item", id="부드러운_신발", name="부드러운 신발", description="소리를 내지 않고 걸을 수 있는 푹신한 신발입니다.")

    b "Let's move to the next door."
    
    return
