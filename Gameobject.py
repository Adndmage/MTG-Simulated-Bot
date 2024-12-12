class Gameobject:
    def __init__(self, name, card_type, mana_value, power=None, toughness=None):
        self.name = name
        self.card_type = card_type
        self.mana_value = mana_value
        self.is_tapped = False
        
        # Only relevant for creatures
        self.power = power
        self.toughness = toughness
        self.is_attacking = None 
        self.summoning_sick = None
        if self.card_type == "Creature": 
            self.summoning_sick = True
            self.is_attacking = False
    
    def __str__(self):
        return f"{self.name} is of the card type {self.card_type} and has a mana value of {self.mana_value}"

    def tap_object(self):
        if not self.is_tapped:
            self.is_tapped = True
    
    def untap_object(self):
        if self.is_tapped:
            self.is_tapped = False