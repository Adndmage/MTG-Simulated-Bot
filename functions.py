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

def update_board(game, cards):
    card_counter = 0
    for card in game.players[0].hand:
        card.sprite = CardSprite(284 + 115 * card_counter, 822, 0.15, card.name)
        cards.add(card.sprite)
        card_counter += 1
    
    card_counter = 0
    for card in game.players[1].hand:
        card.sprite = CardSprite(284 + 115 * card_counter, 79, 0.15, card.name)
        cards.add(card.sprite)
        card_counter += 1
    
    card_counter = 0
    for card in game.players[0].battlefield:
        card.sprite = CardSprite(290 + 170 * card_counter, 595, 0.18, card.name)
        cards.add(card.sprite)
        card_counter += 1
    
    card_counter = 0
    for card in game.players[1].battlefield:
        card.sprite = CardSprite(290 + 170 * card_counter, 305, 0.18, card.name)
        cards.add(card.sprite)
        card_counter += 1