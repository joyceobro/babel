# Characters
define b = Character("Buddy", color="#ffb6c1")
define p = Character("You", color="#ffffff")

# Game Data
init python:
    class Item:
        def __init__(self, id, name, description, icon=None, effect=None):
            self.id = id
            self.name = name
            self.description = description
            self.icon = icon
            self.effect = effect

    class Sticker:
        def __init__(self, id, name, description, icon=None):
            self.id = id
            self.name = name
            self.description = description
            self.icon = icon

    # Helper function to add reward
    def add_reward(reward_type, id, name, description, icon=None, effect=None):
        if reward_type == "item":
            if not any(item.id == id for item in inventory):
                inventory.append(Item(id, name, description, icon, effect))
                renpy.notify("Got Item: " + name)
        elif reward_type == "sticker":
            if not any(s.id == id for s in stickers):
                stickers.append(Sticker(id, name, description, icon))
                renpy.notify("New Sticker: " + name)

    # Function to use an item
    def use_item(item):
        if item.effect:
            # Play sound effect (if you have one, placeholder for now)
            # renpy.play("audio/item_use.ogg")
            
            if "energy" in item.effect:
                global energy
                energy = min(max_energy, energy + item.effect["energy"])
                
                # Buddy's reaction
                renpy.say(b, f"Wow! You used {item.name}! You look much better now!")
                renpy.notify(f"Energy +{item.effect['energy']}")
            
            # Remove item after use
            inventory.remove(item)
            renpy.restart_interaction()
        else:
            renpy.say(b, "I don't think you can use that right now.")

    def wrong_answer():
        global energy
        energy -= 1
        renpy.notify("Energy -1")
        if energy <= 0:
            renpy.jump("game_over")

# Variables
default inventory = []
default stickers = []
default energy = 10
default max_energy = 20

# Images
image bg_dream_room:
    "images/bg_dream_room.png"
    fit "cover"
    xsize 1920 ysize 1080

image buddy_lovely_happy:
    "images/buddy_lovely_happy.png"
    ysize 800
    xalign 0.5
    yalign 1.0

image stage1_bg:
    "images/stage1.png"
    fit "cover"
    xsize 1920 ysize 1080

image stage2_bg:
    "images/stage2.png"
    fit "cover"
    xsize 1920 ysize 1080

image stage3_bg:
    "images/stage3.png"
    fit "cover"
    xsize 1920 ysize 1080

image stage4_bg:
    "images/stage4.png"
    fit "cover"
    xsize 1920 ysize 1080

# Game start
label start:
    $ energy = 10 # Reset energy at start
    show screen energy_bar # Use the new energy_bar screen for better visibility or update existing
    
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

label game_over:
    scene black with fade
    "Energy reached zero..."
    "Buddy tries to wake you up, but you are too tired to move."
    b "Oh no! Wake up! Please..."
    
    menu:
        "Restart from the beginning":
            jump start
        "Quit":
            $ renpy.quit()
    return
