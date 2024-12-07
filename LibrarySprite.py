import pygame as pg
from Gameobject import *

class LibrarySprite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load(f'images/cards/cardback.jpeg')
        self.image = pg.transform.rotozoom(self.image, 0, 0.15)
        self.rect = self.image.get_rect(midleft = (50, 560))