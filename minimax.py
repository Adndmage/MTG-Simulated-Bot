from Game import *

def minimax(game, depth, is_maximizing_player):
    if depth == 0 or not game.is_running:
        return evaluate(game)

    if is_maximizing_player:
        max_evaluation = -10000

        for action_integer in range(1, 7):
            game.perform_gameaction(action_integer)
            evaluation = minimax(game, depth - 1, False)
            max_evaluation = max(max_evaluation, evaluation)
        return max_evaluation
    else:
        min_evaluation = 10000

        for action_integer in range(1, 7):
            game.perform_gameaction(action_integer)
            evaluation = minimax(game, depth - 1, True)
            min_evaluation = min(min_evaluation, evaluation)
        return min_evaluation


def evaluate(game):
    evaluation = game.players[1].life_total - game.players[0].life_total
    evaluation += 2*len(game.players[1].hand) - 2*len(game.players[0].hand)

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