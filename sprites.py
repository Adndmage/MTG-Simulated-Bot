import pygame as pg

# Sprite for all card fronts
class CardSprite(pg.sprite.Sprite):
    def __init__(self, x, y, zoom, name, is_tapped=False):
        super().__init__()
        self.name = name
        self.is_tapped = is_tapped
        self.image = pg.image.load(f'images/cards/{self.name}.png')

        if self.is_tapped:
            self.image = pg.transform.rotozoom(self.image, -90, zoom)
        else:
            self.image = pg.transform.rotozoom(self.image, 0, zoom)

        self.rect = self.image.get_rect(midleft = (x, y))

# Sprite for mtg card back
class LibrarySprite(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load(f'images/cards/cardback.jpeg')
        self.image = pg.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center = (x, y))

class FontSprite(pg.sprite.Sprite):
    def __init__(self, x, y, text, font_name, font_size, placement = "center", color = '#000000'):
        super().__init__()
        
        font = pg.font.SysFont(font_name, font_size)
        self.image = font.render(text, False, color)
        self.rect = self.rect = self.image.get_rect(midleft = (x, y))

        if placement == "midleft":
            self.rect = self.image.get_rect(midleft = (x, y))
        elif placement == "center":
            self.rect = self.image.get_rect(center = (x, y))
        elif placement == "midbottom":
            self.rect = self.image.get_rect(midbottom = (x, y))
        elif placement == "midtop":
            self.rect = self.image.get_rect(midtop = (x, y))