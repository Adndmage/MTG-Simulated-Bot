import pygame as pg
from Game import *
from Player import *

# Function for setting the game up
def setup_game():
    # Creates 2 players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Shuffles the players libraries
    player1.shuffle_library()
    player2.shuffle_library()

    # Draws starting hands
    for _ in range(7):
        player1.draw_card()
        player2.draw_card()
    
    # Returns game class with the players to be stored in a variable
    return Game(player1, player2)