from operator import truediv
import os
import random

import pygame as pg
import main
import classes

def main():
    pg.init()

    screen = pg.display.set_mode((480,240))

    running = True

    while running:
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                running = False

if __name__ == "__main__":
    main()
