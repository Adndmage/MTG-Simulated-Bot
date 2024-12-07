import pygame as pg
from Gameobject import *
from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.life_total = 20
        self.library = (
            [Gameobject('Mountain', 'Land', 0)] * 16 + 
            [Gameobject('Hulking Goblin', 'Creature', 2, power=2, toughness=2)] * 12 +
            [Gameobject('Lightning Bolt', 'Instant', 1)] * 12
        )
        self.hand = []
        self.battlefield = []
        self.priority_passed = False
    
    # def addToLibrary(self, Card):
    #     self.library.append(Card)

    def shuffle_library(self):
        shuffle(self.library)

    def draw_card(self):
        if self.library:
            self.hand.append(self.library.pop())
    
    def play_mountain(self):
        # if land has not been played this turn and it is currently the players turn also check if the player has a mountain in hand
        # mountains = [card for card in self.hand if card.name == "Mountain"]
        mountain = next((card for card in self.hand if card.name == "Mountain"), None)
        
        if mountain:
            self.hand.remove(mountain)
            self.battlefield.append(mountain)
    
    def play_hulking_goblin(self): # WIP
        # Implement check for number of untapped mana in play and tapping said mountains
        hulking_goblins = [card for card in self.hand if card.name == "Hulking Goblin"]
        self.hand.remove(hulking_goblins[0])
        self.battlefield.append(hulking_goblins[0])
    
    def play_lightning_bolt(self):
        # see above for removing card from hand
        lightning_bolts = [card for card in self.hand if card.name == "Lightning Bolt"]
        self.hand.remove(lightning_bolts[0])
        self.battlefield.append(lightning_bolts[0])
    
    def remove_creature(self):
        # List comprehension to find and remove gobbo
        hulking_goblins = [card for card in self.battlefield if card.name == "Hulking Goblin"]
        self.battlefield.remove(hulking_goblins[0])
        # Append to graveyard
    
    def attack_with_all(self):
        # List comprehension to find all gobbos on battlefield
        for card in self.battlefield:
            if card.name == "Hulking Goblin":
                card.Tap_object()