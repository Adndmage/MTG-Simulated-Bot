import pygame as pg
from sprites import CardSprite

class Gameobject:
    # Default values for power and toughness are used if the card isn't a creature
    def __init__(self, name, card_type, mana_value, power=None, toughness=None):
        self.name = name
        self.card_type = card_type
        self.mana_value = mana_value
        self.is_in_hand = True
        self.is_tapped = False
        # self.actions = []
        # self.action_list = []
        self.sprite = None
    
    def __str__(self):
        return f'{self.name}'
    
    # Taps the object if it isn't tapped
    def tap_object(self):
        if not self.is_tapped and self.sprite:
            self.is_tapped = True
            self.image = pg.transform.rotozoom(self.image, -90, 1)
    
    # Untaps the object if it is tapped
    def untap_object(self):
        if self.is_tapped and self.sprite:
            self.is_tapped = False
            self.image = pg.transform.rotozoom(self.image, 90, 1)

    # Potential functionality for tying game actions to specific cards    
    # def add_action(self, action):
    #     self.actions.append(action)