import pygame as pg
from Gameobject import *
from Player import *
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.turn = randint(0, 1) # Assigns the starting player by randomly picking an integer, which can later be used with self.players to determine which player's turn it is
        self.priority = self.turn # Assigns the priority to the current player
        self.phase = "Draw"
    
    # Passes the turn to the other player
    def pass_turn(self):
        self.turn = (self.turn + 1) % 2 # 0 becomes 1 and 1 becomes 0
    
    # Changes phases in the turn
    def change_phase(self):
        phases = ["Draw", "Main 1", "Attackers", "Damage", "Main 2"] # List of phases. Combat is divided into attackers and damage. Blockers can be added later.

        current_phase_index = phases.index(self.phase) # Finds the index of the current phase in the phases list
        self.phase = phases[(current_phase_index + 1) % len(phases)] # Adds 1 to the index or resets it if it has reached the end

        if self.phase == "Draw": # If the new phase is "Draw" then it must be a new turn
            self.pass_turn()
            self.players[self.turn].draw_card() # Draws a card
    
    # Passes the priority to the other player
    def pass_priority(self, player):
        # Logs that this player has passed priority
        player.priority_passed = True
        self.priority = (self.priority + 1) % 2 # 0 becomes 1 and 1 becomes 0

        # If both players have passed priority the game changes phases and priority_passed attributes reset
        if self.players[0].priority_passed == True and self.players[1].priority_passed == True:
            self.players[0].priority_passed = False
            self.players[1].priority_passed = False
            self.change_phase()
        
        return True
    
    # Checks if the game has been won/lost
    def check_gameover(self):
        # Checks if either players life total is 0 or less
        for player in self.players:
            if player.life_total <= 0:
                print(f'{player.name} has lost the game!')
                return True
        return False

    # Performs a game action based on an input from the player (see main)
    def perform_gameaction(self, actionInputInteger):
        player = self.players[self.priority]

        can_action_be_performed = None

        # Based on the integer value a specific action is performed
        if actionInputInteger == 1:
            can_action_be_performed = self.pass_priority(player)
        elif actionInputInteger == 2:
            can_action_be_performed = player.play_mountain()
        elif actionInputInteger == 3:
            can_action_be_performed = player.play_hulking_goblin()
        elif actionInputInteger == 4:
            can_action_be_performed = self.play_lightning_bolt_destroy(player)
        elif actionInputInteger == 5:
            can_action_be_performed = self.play_lightning_bolt_damage(player)
        elif actionInputInteger == 6:
            can_action_be_performed = player.attack_with_all()
        # elif actionInputInteger == 6: # Implementation of blocking
        #     self.block_with_all_possible(player)

        if can_action_be_performed:
            print("Action has been performed")
        else:
            print("Action cannot be performed")
    
    # Plays a lightning bolt and destroys a creature
    def play_lightning_bolt_destroy(self, player):
        opponent = None
        for other_player in self.players:
            if other_player != player:
                opponent = other_player
        
        # if opponent.

        has_bolt_been_played = player.play_lightning_bolt()

        # If statement needs to be added if mana check is within the player method
        if has_bolt_been_played:
            for other_player in self.players:
                if other_player != player:
                    other_player.remove_creature()
        else:
            return False
    
    # Plays a lightning bolt dealing damage to the opponent
    def play_lightning_bolt_damage(self, player):
        has_bolt_been_played = player.play_lightning_bolt()

        if has_bolt_been_played:
            for other_player in self.players:
                if other_player != player:
                    other_player.life_total -= 3
                    self.check_gameover()
        else:
            return False