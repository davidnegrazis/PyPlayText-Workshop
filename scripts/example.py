from sys import exit

# ------------------------------------------------------------------------------
global dev_name
global game_title
dev_name = "Dave" # enter your name in the quotes!
game_title = "Defeat Jacob!" # enter the game title in the quotes!
# ------------------------------------------------------------------------------


# ---------- initial values ----------
# these are used to define the starting values of your game variables
init_health = 100
init_mana = 50
init_boss_health = 50
init_has_sword = False



# ---------- game variables ----------
# these will be used during the game
health = 0
mana = 0
boss_health = 0
has_sword = 0


# ---------- some useful functions ----------
# initialize game variables
def init():
    global has_sword
    global health
    global boss_health
    global mana
    
    health = init_health
    mana = init_mana
    boss_health = init_boss_health
    has_sword = init_has_sword
    
# game over
def game_over(msg):
    print(msg)
    print("Play again? (y / n)")
    while (True):
        choice = input("> ")
        if (choice == "y"):
            start()
            break
        elif (choice == "n"):
            exit(0)
        else:
            print("Options: y / n")


# ---------- room definitions ----------
# here is where you'll create the flow of the game!

# room 0: where the game starts
def room_0():
    global has_sword
    
    print("You are currently sitting in the lounge at 360insights.")
    print("There is a door to the east.")
    
    if has_sword == False:
        print("In front of you is a sword.")

    while(True):
        choice = input("> ");
        
        if "east" in choice:
            room_1()
            break
        elif "take sword" in choice and has_sword == False:
            print("Sword taken!")
            has_sword = True
        else:
            print("Invalid command!")

def room_1():
    print("You are in the hallway now.")
    print("North of you is a nerdy looking guy.")
    print("To the south, there is something that looks interesting.")
    
    while(True):
        choice = input("> ");
        
        if "north" in choice:
            room_2()
            break
        elif "south" in choice:
            game_over("It was a trap!")
            break
        elif "west" in choice:
            room_0()
            break
        else:
            print("Invalid command!")
                
def room_2():
    global has_sword
    global health
    global boss_health
    global mana
    
    valid_commands = ["attack", "block", "do nothing"]
    
    print("Uh oh! It's a boss battle with Jacob!")
    print("Either attack, block, or do nothing!")
    
    while(True):
        choice = input("> ");
        
        if "attack" in choice:
            if (has_sword):
                boss_health -= 20
                print("You used your sword to attack Jacob for 20 attack damage!")
            else:
                boss_health -= 10
                print("You used your first to attack Jacob for 10 attack damage!")
            
            health -= 20
            print("Jacob attacked you, dealing 20 damage!")
        elif "block" in choice:
            if mana > 15:
                health += 10
                mana -= 15
                print("You healed 10 points of health, costing 15 mana")
            else:
                health -= 40
                print("You don't have enough mana!")
                print("Jacob super attacked you, dealing 50 attack damage!")
                
        elif "do nothing" in choice:
            health -= 30
            print("Jacob attacked you, dealing 30 damage!")
        else:
            print("Invalid command")
            
        if choice in valid_commands:
            print("Your health: " + str(max(health, 0)))
            print("Jacob's health: " + str(max(boss_health, 0)))
            print("Remaining mana: " + str(mana))
            
        if (health <= 0 and boss_health <= 0):
            game_over("You both died at the same time...")
            break
        elif (health <= 0):
            game_over("You've been defeated by the formidable Jacob...")
            break
        elif (boss_health <= 0):
            game_over("You have defeated the formidable Jacob! Well done!")
            break
            


def start():
    start_msg = "Now playing " + game_title + " by " + dev_name
    print(start_msg)
    init()
    room_0()


# ---------- game start ----------
start()
