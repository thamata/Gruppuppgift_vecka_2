from email.policy import default
import game


def printC(str):
    print(f'''-----------------------------------------------
{str}
-----------------------------------------------''')

running = False
game_map = game.Map()
game_player = game.Player()

info = '''Game prompts: 
>>[This means that the game is waiting for your input, input is not case sensitive]
//[The text after these signs indicate a game message]'''

printC(f"Game info!\nThis is the map: \n{game_map}\nYour current position on the map is: [0]\n\n{info}\n\nTo start the game type [start]\nTo exit the game type [exit] during any input prompt")

while True:
    initial_input = input(str(">>"))
    if(initial_input.lower() == "start"):
        running = True
        break
    elif(initial_input.lower() == "exit"):
        break
    else:
        print("//Invalid input")

def player_input():
    global running
    printC("//Which direction do you want to move: [right] [left] [up] [down]")
    direction = input(str(">>"))
    match direction.lower():
        case "right":
            game_map.moveRight()
        case "left":
            game_map.moveLeft()
        case "up":
            game_map.moveUp()
        case "down":
            game_map.moveDown()
        case "exit":
            running = False
        case _:
            print("//Invalid input")
    printC(f"{game_map}\n//Your current position on the map is: [{game_map.currentpos}]")

while running:
    player_input()
    print(game_map.dialog())
    continue