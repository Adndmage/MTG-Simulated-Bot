from Game import *
from copy import deepcopy

def computer_ai(game):
    best_evaluation = -10000
    best_action = None
    # list_of_actions = game.get_possible_actions(1)
    # print(list_of_actions)

    for action_integer in game.get_possible_actions(1):
        game_copy = deepcopy(game)
        game_copy.perform_gameaction(action_integer)
        evaluation = minimax(game_copy, 8, False)
        
        if evaluation > best_evaluation:
            best_evaluation = evaluation
            best_action = action_integer
    # print(f'Best action: {best_action}')
    # print(f'Best evaluation: {best_evaluation}')
    return best_action

def minimax(game, depth, is_maximizing_player):
    if depth == 0 or not game.is_running:
        return evaluate(game)

    current_player = 1 if is_maximizing_player else 0

    if is_maximizing_player:
        max_evaluation = -10000

        for action_integer in game.get_possible_actions(current_player):
            game_copy = deepcopy(game)
            game_copy.perform_gameaction(action_integer)
            evaluation = minimax(game, depth - 1, False)
            max_evaluation = max(max_evaluation, evaluation)
        return max_evaluation
    else:
        min_evaluation = 10000

        for action_integer in game.get_possible_actions(current_player):
            game_copy = deepcopy(game)
            game_copy.perform_gameaction(action_integer)
            evaluation = minimax(game, depth - 1, True)
            min_evaluation = min(min_evaluation, evaluation)
        return min_evaluation


def evaluate(game):
    evaluation = game.players[1].life_total - game.players[0].life_total
    evaluation += len(game.players[1].hand) - len(game.players[0].hand)

    for card in game.players[1].battlefield:
        if card.name == "Mountain":
            evaluation += 2
        if card.name == "Hulking Goblin":
            evaluation += 4
    
    for card in game.players[0].battlefield:
        if card.name == "Mountain":
            evaluation -= 2
        if card.name == "Hulking Goblin":
            evaluation -= 4

    return evaluation