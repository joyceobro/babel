# Stage 3: 멈춰선 로봇 (The Sleeping Robot)

label stage_3:
    scene stage3_bg with fade
    
    "A large robot is standing in the middle of the hallway, blocking the path. Its eyes are dark; it seems to be sleeping."
    
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
                jump s3_q1
            "Stop!":
                b "Correct! It stops moving."
            "Go!":
                b "No, it will keep going! Try again."
                jump s3_q1

    # Question 2
    label s3_q2:
        b "How do you tell the robot to 'Sit down'?"
        menu:
            "Sit down!":
                b "Yes! Good command."
            "Stand up!":
                b "No, that makes it stand! Try again."
                jump s3_q2
            "Jump!":
                b "No, we don't want it to jump! Try again."
                jump s3_q2

    # Question 3
    label s3_q3:
        b "What does 'Don't move' mean?"
        menu:
            "움직이지 마.":
                b "That's right! Stay still."
            "노래하지 마.":
                b "No, that's 'Don't sing'. Try again."
                jump s3_q3
            "뛰지 마.":
                b "No, that's 'Don't run'. Try again."
                jump s3_q3

    # Reward and ending of stage 3
    b "Whew, it didn't wake up! You are a natural leader."
    
    "You got a Stop Remote to pause robots."
    "You received Soft Shoes to walk quietly."

    b "Let's move to the next door."
    
    return
