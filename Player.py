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
        # Generator expression and next() is used to find the first mountain in hand
        mountain = next((card for card in self.hand if card.name == "Mountain"), None)
        
        # Checks to see if a mountain has been found in hand and if a land has been played this turn
        if mountain: # and variable to check if land has been played this turn
            self.hand.remove(mountain)
            self.battlefield.append(mountain)
        else:
            print("Action cannot be performed")
    
    def play_hulking_goblin(self):
        hulking_goblin = next((card for card in self.hand if card.name == "Hulking Goblin"), None)

        if hulking_goblin: # and mana check
            self.hand.remove(hulking_goblin)
            self.battlefield.append(hulking_goblin)
        else:
            print("Action cannot be performed")
    
    def play_lightning_bolt(self):
        lightning_bolt = next((card for card in self.hand if card.name == "Lightning Bolt"), None)

        if lightning_bolt: # and mana check
            self.hand.remove(lightning_bolt)
            self.battlefield.append(lightning_bolt)
        else:
            print("Action cannot be performed")
    
    def remove_creature(self):
        hulking_goblin = next((card for card in self.hand if card.name == "Hulking Goblin"), None)
        self.battlefield.remove(hulking_goblin)
        # Append to graveyard
    
    def attack_with_all(self):
        # List comprehension to find all gobbos on battlefield
        for card in self.battlefield:
            if card.name == "Hulking Goblin":
                card.Tap_object()