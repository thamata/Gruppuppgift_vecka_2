import game


def printC(str):
    print(f'''
    -----------------------------------------------
    >>{str}
    -----------------------------------------------
    ''')

running = False

'''printC("Type start to start the game")
input = input()
if(input.lower() == "start"):
    printC("Game started")
    running = True'''

mapM = game.Map()
playerP = game.Player()
#mapM.moveRight()
currentpos = mapM.getPos()

printC(f"Map:\n{mapM}")

print(currentpos)

print(mapM.dialog())
print(playerP.health)
#printC(game.Dialog)