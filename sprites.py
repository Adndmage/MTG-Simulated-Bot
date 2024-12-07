import pygame as pg
from Gameobject import *

# Sprite for the library mtg card back
class LibrarySprite(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load(f'images/cards/cardback.jpeg')
        self.image = pg.transform.rotozoom(self.image, 0, 0.18)
        self.rect = self.image.get_rect(center = (x, y))

class FontSprite(pg.sprite.Sprite):
    def __init__(self, x, y, text, font, placement = "center", color = '#000000'):
        super().__init__()

        self.image = font.render(text, False, color)
        self.rect = self.rect = self.image.get_rect(midleft = (x, y))

        if placement == "midleft":
            self.rect = self.image.get_rect(midleft = (x, y))
        elif placement == "center":
            self.rect = self.image.get_rect(center = (x, y))
        