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
        ) # Makes deck consisting of 16 lands, 12 creatures and 12 bolts
        self.hand = [] # Player's hand
        self.battlefield = [] # Cards on the battlefield
        self.priority_passed = False # Checks if player has passed priority in the current phase

    # Shuffles cards in library
    def shuffle_library(self):
        shuffle(self.library)

    # Takes the top of the library and puts it into the player's hand
    def draw_card(self):
        if self.library:
            self.hand.append(self.library.pop())
    
    # Takes a mountain from hand and puts it onto the battlefield
    def play_mountain(self):
        # if land has not been played this turn and it is currently the players turn also check if the player has a mountain in hand
        # Generator expression and next() is used to find the first mountain in hand
        mountain = next((card for card in self.hand if card.name == "Mountain"), None)
        
        # Checks to see if a mountain has been found in hand and if a land has been played this turn
        if mountain: # and variable to check if land has been played this turn
            self.hand.remove(mountain)
            self.battlefield.append(mountain)
            return True
        else:
            return False
    
    # Takes a creature from hand and puts it onto the battlefield
    def play_hulking_goblin(self):
        hulking_goblin = next((card for card in self.hand if card.name == "Hulking Goblin"), None)

        if hulking_goblin: # and mana check
            self.hand.remove(hulking_goblin)
            self.battlefield.append(hulking_goblin)
            return True
        else:
            return False
    
    # Takes a bolt from hand and puts it onto the battlefield
    def play_lightning_bolt(self):
        lightning_bolt = next((card for card in self.hand if card.name == "Lightning Bolt"), None)

        if lightning_bolt: # and mana check
            self.hand.remove(lightning_bolt)
            return True
        else:
            print("Action cannot be performed")
            return False
    
    # Removes a creature from the battlefield
    # Since all creatures are the same there is no need to differentiate
    def remove_creature(self):
        hulking_goblin = next((card for card in self.hand if card.name == "Hulking Goblin"), None)

        if hulking_goblin:
            self.battlefield.remove(hulking_goblin)
            return True
        else:
            return False
        # Append to graveyard
    
    # Takes every creature on the side of the current player and attacks with them
    # Add functionality for the player to decide how many creatures to attack with
    def attack_with_all(self):
        # Takes every creature and taps it
        for card in self.battlefield:
            if card.name == "Hulking Goblin":
                card.tap_object()
        
        return True