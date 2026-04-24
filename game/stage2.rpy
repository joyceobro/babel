# Stage 2: 어두운 복도 (The Dark Hallway)

label stage_2:
    scene stage2_bg with fade
    
    "Following Buddy, I stepped out of the room. The hallway is very long and dark."
    
    show buddy_lovely_happy at center with dissolve
    
    b "How are you? Are you okay?"
    
    p "I am a little scared. It is very dark."
    
    b "I am happy because I am with you! Look, I have a small light."
    
    p "That is good. I am hungry, too."
    
    b "Don't worry. We can find some bread soon!"

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
                jump s2_q1
            "Hello, Buddy.":
                b "Hello, but I asked how you are! Try again."
                jump s2_q1

    # Question 2
    label s2_q2:
        b "What does 'I am hungry' mean?"
        menu:
            "졸려요.":
                b "No, that's 'I am sleepy'. Try again."
                jump s2_q2
            "배고파요.":
                b "Correct! We need food."
            "심심해요.":
                b "No, that's 'I am bored'. Try again."
                jump s2_q2

    # Question 3
    label s2_q3:
        b "Why did I say 'I am happy'?"
        menu:
            "Because I am alone":
                b "No, I like being with friends! Try again."
                jump s2_q3
            "Because I slept":
                b "No, that's not it. Try again."
                jump s2_q3
            "Because I am with you":
                b "Yes! I am happy because we are together."

    # Reward and ending of stage 2
    b "You are doing great! Let's keep going."
    
    "You got a Small Flashlight to light up the dark."
    "You earned the Badge of Courage!"

    b "Shhh, I hear a robot moving!"
    
    return
