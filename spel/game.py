import numpy as np

class Player:
    health = 100

class Map:
    def __init__(self):
        self.grid = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

        self.currentpos = self.grid[1][0]
    
    def moveRight(self):
        toMove = 0
        for n in range(3):
            if(self.currentpos != self.grid[n][3]):
                toMove = 1
            else:
                return print("you cannot move further right")
        self.currentpos += toMove

    def moveLeft(self):
        toMove = 0
        for n in range(3):
            if(self.currentpos != self.grid[n][0]):
                toMove = 1
            else:
                return print("you cannot move further left")
        self.currentpos -= toMove

    def moveDown(self):
        if(self.currentpos <= 11):
            self.currentpos += 4
        else:
            return print("you cannot move further down")
    def moveUp(self):
        if(self.currentpos >= 4):
            self.currentpos -= 4
        else:
            return print("you cannot move further up")

instans = Map()

print(instans.grid)
print("pos:", instans.currentpos)
instans.moveRight()
print("pos:", instans.currentpos)
instans.moveRight()
print("pos:", instans.currentpos)
instans.moveRight()
print("pos:", instans.currentpos)
instans.moveRight()
print("pos:", instans.currentpos)

instans.moveLeft()
print("pos:", instans.currentpos)
instans.moveLeft()
print("pos:", instans.currentpos)
instans.moveLeft()
print("pos:", instans.currentpos)
instans.moveLeft()
print("pos:", instans.currentpos)