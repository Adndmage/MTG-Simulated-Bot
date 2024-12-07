import pygame as pg
from Gameobject import *

# Possible implementation of abilities tied to the individual cards
class Mountain(Gameobject):
    def __init__(self, name, card_type, mana_value=0):
        super().__init__(name, card_type, mana_value)