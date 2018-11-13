from sys import exit

# ------------------------------------------------------------------------------
global dev_name
global game_title
dev_name = "" # enter your name in the quotes!
game_title = "" # enter the game title in the quotes!
# ------------------------------------------------------------------------------


# ---------- initial values ----------
# these are used to define the starting values of your game variables
global init_health
global init_mana
global boss_health
init_health = 100
init_mana = 200
init_boss_health = 50


# ---------- game variables ----------
# these will be used during the game
global health
global mana
global boss_health


# ---------- some useful functions ----------
# initialize game variables
def init():
    health = init_health
    mana = init_mana
    
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
    print("This is the first stage of the game. Create a custom description and get coding!")

    choice = input("> ");

    if "end" in choice:
        game_over("The game is over")


def start():
    start_msg = "Now playing " + game_title + " by " + dev_name
    print(start_msg)
    init()
    room_0()


# ---------- game start ----------
start()
