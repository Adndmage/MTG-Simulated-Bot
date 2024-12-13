from Game import *
from copy import deepcopy

count = 0

def computer_ai(game, player_integer):
    global count
    count = 0

    action_list = game.get_possible_actions(player_integer)
    if len(action_list) == 1:
        return action_list[0]

    if player_integer == 1:
        best_evaluation = -10000
        best_action = None

        for action_integer in action_list:
            game_copy = deepcopy(game)
            game_copy.is_temporary = True
            game_copy.perform_gameaction(action_integer)
            evaluation = minimax(game_copy, 15, -10000, 10000, False)
            
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_action = action_integer
        print(count)
        return best_action
    else:
        best_evaluation = 10000
        best_action = None

        for action_integer in action_list:
            game_copy = deepcopy(game)
            game_copy.is_temporary = True
            game_copy.perform_gameaction(action_integer)
            evaluation = minimax(game_copy, 15, -10000, 10000, True)
            
            if evaluation < best_evaluation:
                best_evaluation = evaluation
                best_action = action_integer
        print(count)
        return best_action

def minimax(game, depth, alpha, beta, is_maximizing_player):
    global count
    count += 1

    if depth == 0 or not game.is_running:
        return evaluate(game)

    current_player = 1 if is_maximizing_player else 0

    if is_maximizing_player:
        max_evaluation = -10000

        for action in game.get_possible_actions(current_player):
            game_copy = deepcopy(game)
            game_copy.perform_gameaction(action)
            evaluation = minimax(game_copy, depth - 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, max_evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = 10000

        for action in game.get_possible_actions(current_player):
            game_copy = deepcopy(game)
            game_copy.perform_gameaction(action)
            evaluation = minimax(game_copy, depth - 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, min_evaluation)
            if beta <= alpha:
                break
        return min_evaluation

def evaluate(game):
    if game.players[1].life_total <= 0:
        return -1000
    elif game.players[0].life_total <= 0:
        return 1000

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