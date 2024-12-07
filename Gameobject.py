import pygame as pg

class Gameobject(pg.sprite.Sprite):
    def __init__(self, name, card_type, mana_value, power=None, toughness=None):
        super().__init__()
        self.name = name
        self.card_type = card_type
        self.mana_value = mana_value
        self.is_in_hand = True
        self.is_tapped = False
        self.actions = []
        self.action_list = []

        self.image = pg.image.load(f'images/cards/{self.name}.png')
        self.image = pg.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(midbottom = (400, 720))
    
    def __str__(self):
        return f'{self.name}'
    
    def tap_object(self):
        if not self.is_tapped:
            self.is_tapped = True
            self.image = pg.transform.rotozoom(self.image, -90, 1)
    
    def untap_object(self):
        if self.is_tapped:
            self.is_tapped = False
            self.image = pg.transform.rotozoom(self.image, 90, 1)
    
    def add_action(self, action):
        self.actions.append(action)
    
    def update(self):
        self.tap_object()