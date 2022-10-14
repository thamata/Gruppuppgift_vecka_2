import game


def printC(str):
    print(f'''-----------------------------------------------
{str}
-----------------------------------------------''')

running = False
game_map = game.Map()
game_player = game.Player()
enemy_gargoyle = game.Enemy("Gargoyle", 20, 3)
enemy_dog = game.Enemy("Dog", 10, 5)
enemy_RabidDog = game.Enemy("Rabid dog", 10, 10)
clearedGrids = [0]


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
    printC(f"{game_map}\n//Your current position on the map is: [{game_map.getPos()}]")

def grid_battle():
    if(game_map.currentpos in clearedGrids):
        print("Grid cleared")
    elif((game_map.currentpos in clearedGrids) == False):
            print("Grid Not cleared")
            match game_map.currentpos:
                case 1 | 2 | 3 | 4:
                    print(f"You encountered a {enemy_gargoyle.name}")
                    enemy_gargoyle.battle(game_player.attack, game_player.health)
                    print(f"Eh{enemy_gargoyle.health}")
            clearedGrids.append(game_map.currentpos)

while running:
    player_input()
    grid_battle()
    continue