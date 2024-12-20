from Gameobject import *
from Player import *
from random import randint

class Game:
    def __init__(self, player_1, player_2):
        self.players = [player_1, player_2]
        self.__turn = randint(0, 1) # Randomly assigns starting player
        self.__priority = self.__turn
        self.__phase = "Draw"
        self.is_running = True
        self.__is_copy = False
        self.__log_actions = True
    
    def __str__(self):
        return f"It is currently {self.players[self.__turn]}'s turn in the {self.__phase} phase"

    def get_turn(self):
        return self.__turn

    def get_priority(self):
        return self.__priority

    def get_phase(self):
        return self.__phase
    
    def turn_to_copy(self):
        self.__is_copy = True
    
    def pass_turn(self):
        self.__turn = (self.__turn + 1) % 2 # 0 becomes 1, 1 becomes 0
        self.__priority = self.__turn
        self.players[0].land_has_been_played = False
        self.players[1].land_has_been_played = False
        self.players[self.__turn].draw_card()

        # Untaps everything and removes summoning sickness
        for card in self.players[self.__turn].battlefield:
            card.is_tapped = False

            if card.card_type == "Creature": card.summoning_sick = False

    def change_phase(self):
        phases = ["Draw", "Main 1", "Attackers", "Damage", "Main 2", "End"]

        current_phase_index = phases.index(self.__phase)
        self.__phase = phases[(current_phase_index + 1) % len(phases)] # Adds 1 to the index or resets it if it has reached the end

        if self.__phase == "Draw": # If the new phase is "Draw" then it must be a new turn
            self.pass_turn()
        
        if self.__phase == "Main 2": # If the new the phase is "Main 2" the previous phase was "Damage"
            self.combat_damage()
    
    def pass_priority(self, player):
        player.priority_passed = True # Logs that this player has passed priority
        self.__priority = (self.__priority + 1) % 2 # 0 becomes 1, 1 becomes 0

        # If both players have passed priority the game changes phases
        if self.players[0].priority_passed == True and self.players[1].priority_passed == True:
            self.players[0].priority_passed = False
            self.players[1].priority_passed = False
            self.change_phase()
    
    def check_gameover(self):
        for player in self.players:
            if player.life_total <= 0:
                if not self.__is_copy: print(f"{player.name} has lost the game!")
                self.is_running = False

    def combat_damage(self):
        opponent = self.players[(self.__turn + 1) % 2]

        for card in self.players[self.__turn].battlefield:
            if card.is_tapped and card.power:
                opponent.life_total -= card.power
        self.check_gameover()
    
    def get_possible_actions(self, player_integer):
        action_list = []

        # Checks hand and battlefield for the specific cards
        mountain = next((card for card in self.players[player_integer].hand if card.name == "Mountain"), None)
        lightning_bolt = next((card for card in self.players[player_integer].hand if card.name == "Lightning Bolt"), None)
        hulking_goblin_hand = next((card for card in self.players[player_integer].hand if card.name == "Hulking Goblin"), None)
        hulking_goblin_battlefield = next((card for card in self.players[player_integer].battlefield if card.name == "Hulking Goblin" and not card.summoning_sick), None)
        hulking_goblin_battlefield_opponent = next((card for card in self.players[(player_integer + 1) % 2].battlefield if card.name == "Hulking Goblin"), None)
        
        # Ordering of actions based on what is most likely to be good generally
        if hulking_goblin_battlefield and self.__turn == player_integer and self.__phase == "Attackers":
            action_list.append(6)

        if mountain and not self.players[player_integer].land_has_been_played and self.__turn == player_integer and (self.__phase == "Main 1" or self.__phase == "Main 2"):
            action_list.append(2)
        
        if hulking_goblin_hand and self.players[player_integer].mana_check(2) and self.__turn == player_integer and (self.__phase == "Main 1" or self.__phase == "Main 2"):
            action_list.append(3)

        if lightning_bolt and hulking_goblin_battlefield_opponent and self.players[player_integer].mana_check(1):
                action_list.append(5)

        action_list.append(1)

        if lightning_bolt and self.players[player_integer].mana_check(1):
            action_list.append(4)
        
        return action_list

    def perform_gameaction(self, action_integer):
        player = self.players[self.__priority]
        
        if action_integer not in self.get_possible_actions(self.__priority):
            if self.__log_actions and not self.__is_copy: print(f"Action {action_integer} cannot be performed by {player.name}")
            return

        if action_integer == 1:
            self.pass_priority(player)
            if self.__log_actions and not self.__is_copy: print(f"{player.name} passed priority")

        elif action_integer == 2:
            player.play_mountain()
            if self.__log_actions and not self.__is_copy: print(f"{player.name} played Mountain")

        elif action_integer == 3:
            player.play_hulking_goblin()
            if self.__log_actions and not self.__is_copy: print(f"{player.name} played Hulking Goblin")

        elif action_integer == 4:
            self.play_lightning_bolt_damage(player)
            if self.__log_actions and not self.__is_copy: print(f"{player.name} played Lightning Bolt dealing damage")

        elif action_integer == 5:
            self.play_lightning_bolt_destroy(player)
            if self.__log_actions and not self.__is_copy: print(f"{player.name} played Lightning Bolt destroying a creature")

        elif action_integer == 6:
            player.attack_with_all()
            self.pass_priority(player)
            if self.__log_actions and not self.__is_copy: print(f"{player.name} attacked with all")
    
    # Plays a lightning bolt dealing damage to the opponent
    def play_lightning_bolt_damage(self, player):
        player.play_lightning_bolt()
        opponent = self.players[(self.__priority + 1) % 2]
        opponent.life_total -= 3
        self.check_gameover()
    
    # Plays a lightning bolt and destroys a creature
    def play_lightning_bolt_destroy(self, player):
        player.play_lightning_bolt()
        opponent = self.players[(self.__priority + 1) % 2]
        opponent.remove_creature()