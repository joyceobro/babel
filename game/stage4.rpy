# Stage 4: 신호등 게임 (Open and Close)

label stage_4:
    scene stage4_bg with fade
    
    "We arrived in front of a large iron door. This door is special; it only opens if you say 'Open' or 'Close'."
    
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
                jump s4_q1
            "Hello":
                b "The door doesn't care about greetings! Try again."
                jump s4_q1

    # Question 2
    label s4_q2:
        b "What if you want to close the door?"
        menu:
            "Open":
                b "No, that opens it! Try again."
                jump s4_q2
            "Close":
                b "Correct! It shuts tight."
            "Sit":
                b "The door cannot sit! Try again."
                jump s4_q2

    # Question 3
    label s4_q3:
        b "What does 'fast' mean in 'Say Close very fast'?"
        menu:
            "느리게":
                b "No, that's 'slowly'. Try again."
                jump s4_q3
            "조용히":
                b "No, that's 'quietly'. Try again."
                jump s4_q3
            "빠르게":
                b "Yes! Speed is important."

    # Reward and ending of stage 4
    b "You are getting better at this! Let's go through the door."
    
    "You got a Magic Keychain for luck."
    "You earned the Gatekeeper Sticker!"

    b "Stay sharp!"
    
    return
