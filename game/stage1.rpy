# Stage 1: 깨어난 방 (The Magic Room)

label stage_1:
    play music "audio/stage1_ambient.ogg" loop fadein 2.0

    "I woke up in a dark room. My head feels a little dizzy."
    
    show buddy_lovely_happy at center with dissolve 
    
    b "Hello! Can you hear me? Wake up!"
    
    p "Oh... Who are you?"
    
    b "I am Buddy. I am a helper robot. Don't be afraid!"
    
    p "Where am I? It's so dark here."
    
    b "You are in a big tower. People cannot speak English now. But you can! That is cool!"
    
    p "I want to go home."
    
    b "I can help you. Let's go together. Follow me!"

    "To open the door and leave, you must answer Buddy's questions correctly."

    jump stage_1_quiz

label stage_1_quiz:
    b "First mission! Answer my questions to open the door."

    # Question 1
    label s1_q1:
        b "What does 'Don't be afraid!' mean?"
        menu:
            "배고프지 마!":
                b "No, that's not it. Try again!"
                jump s1_q1
            "무서워하지 마!":
                b "Correct! You are doing great."
            "졸지 마!":
                b "No, that's not it. Try again!"
                jump s1_q1

    # Question 2
    label s1_q2:
        b "What kind of robot am I?"
        menu:
            "A robot that cooks":
                b "No, I can't cook yet! Try again."
                jump s1_q2
            "A robot that fights":
                b "No, I am peaceful! Try again."
                jump s1_q2
            "A robot that helps":
                b "Yes! I am a helper robot."

    # Question 3
    label s1_q3:
        b "What did I say when I asked you to follow me?"
        menu:
            "Follow me!":
                b "That's right! Let's go!"
            "Sit down!":
                b "No, we need to move! Try again."
                jump s1_q3
            "Good bye!":
                b "Not yet! We just met. Try again."
                jump s1_q3

    # Reward and ending of stage 1
    b "Good job! You are very smart."
    
    "Buddy gives you a sparkling candy. (Energy +1)"
    "A 'Genius of English' sticker is placed in your diary."

    b "Now, walk quietly. There is a scary guard robot outside!"
    
    return
