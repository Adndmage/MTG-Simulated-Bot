import pygame as pg
from Game import *
from Player import *

def setup_game():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1.shuffle_library()
    player2.shuffle_library()

    for _ in range(7):
        player1.draw_card()
        player2.draw_card()
    
    return Game(player1, player2)