import game


def printC(str):
    print(f">>{str}")


printC("Type start to start the game")
input = input()
if(input.lower() == "start"):
    printC("Game started")
    game.main()