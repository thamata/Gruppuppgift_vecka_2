import numpy as np

class Player:
    health = 100
    attack = 10

class Map:
    def __init__(self):
        #4x4 grid som array
        self.grid = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

        self.currentpos = self.grid[0][0]
    
    def __str__(self):
        #returnerar mappen som en sträng
        return (str(self.grid))

    def getPos(self):
        #returnerar nuvarande position på mappen
        return self.currentpos

    #flyttar currentpos ett steg till höger
    def moveRight(self):
        toMove = 0
        for n in range(3):
            #bug där pos kan gå över 15
            if(self.currentpos != self.grid[n][3]):
                toMove = 1
            else:
                return print("you cannot move further right")
        self.currentpos += toMove
    #flyttar currentpos ett steg till vänster
    def moveLeft(self):
        toMove = 0
        for n in range(3):
            if(self.currentpos != self.grid[n][0]):
                toMove = 1
            else:
                return print("you cannot move further left")
        self.currentpos -= toMove
    #flyttar currentpos ett steg ner/fyra steg höger
    def moveDown(self):
        if(self.currentpos <= 11):
            self.currentpos += 4
        else:
            return print("you cannot move further down")
    #flyttar currentpos ett steg upp/fyra steg vänster
    def moveUp(self):
        if(self.currentpos >= 4):
            self.currentpos -= 4
        else:
            return print("you cannot move further up")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def battle(self, pAttack, pHealth):
        if(self.health > 0):
            pHealth -= self.attack
            self.health -= pAttack
        elif(self.health <= 0):
            return print("Enemy defeated")
