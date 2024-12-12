from Game import *
from Player import *
from sprites import CardSprite

def setup_game():
    player_1 = Player("Player 1")
    player_2 = Player("AI Bot")

    player_1.shuffle_library()
    player_2.shuffle_library()

    # Draws starting hands
    for _ in range(7):
        player_1.draw_card()
        player_2.draw_card()
    
    return Game(player_1, player_2)

def update_board(game, cards):
    card_counter = 0
    for card in game.players[0].hand:
        cards.add(CardSprite(284 + 115 * card_counter, 822, 0.15, card.name))
        card_counter += 1
    
    card_counter = 0
    for card in game.players[1].hand:
        cards.add(CardSprite(284 + 115 * card_counter, 79, 0.15, card.name))
        card_counter += 1
    
    card_counter = 0
    for card in game.players[0].battlefield:
        if card.name == "Mountain":
            cards.add(CardSprite(290 + 140 * card_counter, 674, 0.12, card.name, card.is_tapped))
            card_counter += 1
    
    card_counter = 0
    for card in game.players[1].battlefield:
        if card.name == "Mountain":
            cards.add(CardSprite(290 + 140 * card_counter, 227, 0.12, card.name, card.is_tapped))
            card_counter += 1
    
    card_counter = 0
    for card in game.players[0].battlefield:
        if card.name == "Hulking Goblin":
            cards.add(CardSprite(290 + 170 * card_counter, 532, 0.15, card.name, card.is_tapped))
            card_counter += 1
    
    card_counter = 0
    for card in game.players[1].battlefield:
        if card.name == "Hulking Goblin":
            cards.add(CardSprite(290 + 170 * card_counter, 369, 0.15, card.name, card.is_tapped))
            card_counter += 1