from random import choice

def computer_random(game):
    game.perform_gameaction(choice(game.get_possible_actions(1)))