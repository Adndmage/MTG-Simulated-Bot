import pygame as pg
from Gameobject import *

class Mountain(Gameobject):
    def __init__(self, name, card_type, mana_value=0):
        super().__init__(name, card_type, mana_value)