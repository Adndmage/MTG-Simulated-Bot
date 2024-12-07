import pygame as pg
from Gameobject import *
from Player import *
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.turn = randint(0, 1)
        self.priority = self.turn
        self.phase = "Draw"
    
    def pass_turn(self):
        self.turn = (self.turn + 1) % 2
    
    def change_phase(self):
        phases = ["Draw", "Main 1", "Attackers", "Damage", "Main 2"]

        current_phase_index = phases.index(self.phase)
        self.phase = phases[(current_phase_index + 1) % len(phases)]

        if self.phase == "Draw":
            self.players[self.turn].draw_card()
    
    def check_gameover(self):
        for player in self.players:
            if player.life_total <= 0:
                print(f'{self.players[self.priority]} has won the game!')
                return True
        return False

    def perform_gameaction(self, player, actionInteger):
        if actionInteger == 0:
            self.pass_priority(player)
        elif actionInteger == 1:
            player.play_mountain()
        elif actionInteger == 2:
            player.play_hulking_goblin()
        elif actionInteger == 3:
            self.play_lightning_bolt_destroy(player)
        elif actionInteger == 4:
            self.play_lightning_bolt_damage(player)
        elif actionInteger == 5:
            player.attack_with_all()
        # elif actionInteger == 6:
        #     self.block_with_all_possible(player)
        else:
            print("Action cannot be performed")
    
    def pass_priority(self, player):
        player.priority_passed = True

        if self.players[0].priority_passed == True and self.players[1].priority_passed == True:
            self.change_phase()
    
    def play_lightning_bolt_destroy(self, player):
        player.play_lightning_bolt

        for other_player in self.players:
            if other_player == player:
                other_player.remove_creature()
    
    def play_lightning_bolt_damage(self, player):
        player.play_lightning_bolt

        for other_player in self.players:
            if other_player == player:
                other_player.life_total -= 3
                self.check_gameover()