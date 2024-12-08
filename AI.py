from time import sleep
from random import randint
from Player import *

def ai(game):
    sleep(1)

    # If it is the ai's turn and it is main phase it will try to do anything unless it has no mana then it will pass unless it's combat then it will attack all
    if not game.players[1].land_has_been_played and game.turn == 1:
        game.perform_gameaction(randint(1, 3))
    else:
        game.perform_gameaction(1)