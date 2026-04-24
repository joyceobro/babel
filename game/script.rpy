# Characters
define b = Character("Buddy", color="#ffb6c1")
define p = Character("You", color="#ffffff")

# Images
image bg_dream_room = "images/bg_dream_room.png"
image buddy_lovely_happy = "images/buddy_lovely_happy.png"
image stage1_bg = "images/stage1.png"
image stage2_bg = "images/stage2.png"
image stage3_bg = "images/stage3.png"
image stage4_bg = "images/stage4.png"

# Game start
label start:
    scene bg_dream_room with fade
    pause 1.0
    
    "I opened my eyes in a strange room..."
    
    scene stage1_bg with dissolve
    
    call stage_1
    call stage_2
    call stage_3
    call stage_4

    "End of Demo. Thanks for playing!"
    
    return
