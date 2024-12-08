class Gameobject:
    # Default values for power and toughness are used if the card isn't a creature
    def __init__(self, name, card_type, mana_value, power=None, toughness=None):
        self.name = name
        self.card_type = card_type
        self.mana_value = mana_value
        self.is_in_hand = True
        self.is_tapped = False
        
        self.power = power
        self.toughness = toughness
        self.is_attacking = None # Polymorfism could be used
        self.summoning_sick = None
        if self.card_type == "Creature": 
            self.summoning_sick = True
            self.is_attacking = False
    
    def __str__(self):
        return f'{self.name}'
    
    # Taps the object if it isn't tapped
    def tap_object(self):
        if not self.is_tapped:
            self.is_tapped = True
    
    # Untaps the object if it is tapped
    def untap_object(self):
        if self.is_tapped:
            self.is_tapped = False