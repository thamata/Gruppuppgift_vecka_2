import game


def printC(str):
    print(f'''
    -----------------------------------------------
    >>{str}
    -----------------------------------------------
    ''')

running = False

printC("Type start to start the game")
input = input()
if(input.lower() == "start"):
    printC("Game started")
    running = True

while running:
