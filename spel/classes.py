import pygame as pg

class Player(pg.sprite.Sprite):

        def __init__(self):
            self.surf = pg.Surface((30, 30))
            self.surf.fill((128,255,40))
            self.rect = self.surf.get_rect(center = (10, 420))