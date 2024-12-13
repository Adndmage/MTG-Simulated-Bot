from Gameobject import *
from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.life_total = 20
        self.library = (
            [Gameobject("Mountain", "Land", 0) for _ in range(16)] +
            [Gameobject("Hulking Goblin", "Creature", 2, power=2, toughness=2) for _ in range(12)] +
            [Gameobject("Lightning Bolt", "Instant", 1) for _ in range(12)]
        )
        self.hand = []
        self.battlefield = []
        self.priority_passed = False # Checks if player has passed priority in the current phase
        self.land_has_been_played = False
    
    def __str__(self):
        return f"{self.name} is at {self.life_total} life"

    def shuffle_library(self):
        shuffle(self.library)

    def draw_card(self):
        if self.library:
            self.hand.append(self.library.pop())
    
    def mana_check(self, mana_value):
        mountains = [land for land in self.battlefield if land.name == "Mountain" and land.is_tapped == False]

        if mana_value <= len(mountains):
            return True
        return False
    
    def mana_pay(self, mana_value):
        mountains = [land for land in self.battlefield if land.name == "Mountain" and land.is_tapped == False]

        for land in mountains[:mana_value]:
            land.tap_object()

    def play_mountain(self):
        # Generator expression and next() is used to find the first mountain in hand
        mountain = next((card for card in self.hand if card.name == "Mountain"), None)

        self.hand.remove(mountain)
        self.battlefield.append(mountain)
        self.land_has_been_played = True

    def play_hulking_goblin(self):
        mana_value = 2
        hulking_goblin = next((card for card in self.hand if card.name == "Hulking Goblin"), None)

        self.mana_pay(mana_value)
        self.hand.remove(hulking_goblin)
        self.battlefield.append(hulking_goblin)

    def play_lightning_bolt(self):
        mana_value = 1
        lightning_bolt = next((card for card in self.hand if card.name == "Lightning Bolt"), None)

        self.mana_pay(mana_value)
        self.hand.remove(lightning_bolt)
    
    def remove_creature(self):
        hulking_goblin = next((card for card in self.battlefield if card.name == "Hulking Goblin"), None)

        self.battlefield.remove(hulking_goblin)

    def attack_with_all(self):
        for card in self.battlefield:
            if card.name == "Hulking Goblin" and not card.summoning_sick:
                card.tap_object()