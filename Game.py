from Gameobject import *
from Player import *
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.turn = randint(0, 1) # Assigns the starting player by randomly picking an integer, which can later be used with self.players to determine which player's turn it is
        self.priority = self.turn
        self.phase = "Draw"
        self.is_running = True
    
    def pass_turn(self):
        self.turn = (self.turn + 1) % 2 # 0 becomes 1 and 1 becomes 0
        self.priority = self.turn
        self.players[0].land_has_been_played = False
        self.players[1].land_has_been_played = False
        self.players[self.turn].draw_card()

        # Untaps everything and removes summoning sickness
        for card in self.players[self.turn].battlefield:
            card.is_tapped = False

            if card.card_type == "Creature": card.summoning_sick = False

    def change_phase(self):
        phases = ["Draw", "Main 1", "Attackers", "Damage", "Main 2", "End"]

        current_phase_index = phases.index(self.phase)
        self.phase = phases[(current_phase_index + 1) % len(phases)] # Adds 1 to the index or resets it if it has reached the end

        if self.phase == "Draw": # If the new phase is "Draw" then it must be a new turn
            self.pass_turn()
        
        if self.phase == "Main 2": # If the previous phase was "Damage"
            self.combat_damage()
    
    def pass_priority(self, player):
        player.priority_passed = True # Logs that this player has passed priority
        self.priority = (self.priority + 1) % 2 # 0 becomes 1 and 1 becomes 0

        # If both players have passed priority the game changes phases and priority_passed attribute resets
        if self.players[0].priority_passed == True and self.players[1].priority_passed == True:
            self.players[0].priority_passed = False
            self.players[1].priority_passed = False
            self.change_phase()
        
        return True
    
    def check_gameover(self):
        opponent = self.players[(self.turn + 1) % 2]
        for player in self.players:
            if player.life_total <= 0:
                print(f'{player.name} has lost the game!')
                self.is_running = False
                # return True
        # return False

    def combat_damage(self):
        opponent = self.players[(self.turn + 1) % 2]
        for creature in self.players[self.turn].battlefield:
            if creature.is_tapped and creature.power:
                opponent.life_total -= creature.power
        self.check_gameover()

    def perform_gameaction(self, actionInputInteger):
        player = self.players[self.priority]

        can_action_be_performed = None

        if actionInputInteger == 1:
            can_action_be_performed = self.pass_priority(player)

        elif actionInputInteger == 2:
            if player == self.players[self.turn] and (self.phase == "Main 1" or self.phase == "Main 2"):
                can_action_be_performed = player.play_mountain()
            else:
                can_action_be_performed = False

        elif actionInputInteger == 3:
            if player == self.players[self.turn] and (self.phase == "Main 1" or self.phase == "Main 2"):
                can_action_be_performed = player.play_hulking_goblin()
            else:
                can_action_be_performed = False

        elif actionInputInteger == 4:
            can_action_be_performed = self.play_lightning_bolt_destroy(player)

        elif actionInputInteger == 5:
            can_action_be_performed = self.play_lightning_bolt_damage(player)

        elif actionInputInteger == 6 and self.phase == "Attackers":
            can_action_be_performed = player.attack_with_all()
        
        # elif actionInputInteger == 6: # Implementation of blocking
        #     self.block_with_all_possible(player)

        if can_action_be_performed:
            print("Action has been performed")
        else:
            print("Action cannot be performed")
    
    # Plays a lightning bolt and destroys a creature
    def play_lightning_bolt_destroy(self, player):
        opponent = self.players[(self.priority + 1) % 2]
        # for other_player in self.players:
        #     if other_player != player:
        #         opponent = other_player
        
        hulking_goblin = next((card for card in opponent.battlefield if card.name == "Hulking Goblin"), None)

        has_bolt_been_played = None
        if hulking_goblin:
            has_bolt_been_played = player.play_lightning_bolt()

        if has_bolt_been_played:
            for other_player in self.players:
                if other_player != player:
                    other_player.remove_creature()
                    return True
        return False
    
    # Plays a lightning bolt dealing damage to the opponent
    def play_lightning_bolt_damage(self, player):
        has_bolt_been_played = player.play_lightning_bolt()
        opponent = self.players[(self.priority + 1) % 2]
        
        if has_bolt_been_played:
            opponent.life_total -= 3
            self.check_gameover()
            return True
        return False