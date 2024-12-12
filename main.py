import pygame as pg
from Gameobject import *
from sprites import *
from functions import *
from minimax import *
from copy import deepcopy
from RandomAI import *

# Pygame standard setup
pg.init()
screen = pg.display.set_mode((1600, 900))
clock = pg.time.Clock()
running = True
game = setup_game()

# Sprites
# Library card backs
library = pg.sprite.Group()
library.add(LibrarySprite(140, 220))
library.add(LibrarySprite(140, 680))

cards = pg.sprite.Group() # Hand and battlefield
dynamic_text = pg.sprite.Group()

# Static text
static_text = pg.sprite.Group()
static_text.add(FontSprite(1440, 30, 'List of', 'lucidasanstypewriter', 40))
static_text.add(FontSprite(1440, 75, 'Game Actions', 'lucidasanstypewriter', 40))
static_text.add(FontSprite(1290, 150, '1: Pass Priority', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1290, 200, '2: Play Mountain', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1290, 250, '3: Play Creature', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1290, 300, '4: Play Bolt Damage', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1290, 350, '5: Play Bolt Destroy', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1290, 400, '6: Attack All', 'lucidasanstypewriterregular', 30, placement="left"))
static_text.add(FontSprite(1444, 500, 'Current Turn:', 'lucidasanstypewriter', 36))
static_text.add(FontSprite(1444, 640, 'Current Phase:', 'lucidasanstypewriter', 36))
static_text.add(FontSprite(140, 890, game.players[0].name, 'lucidasanstypewriterregular', 25, placement="midbottom"))
static_text.add(FontSprite(140, 10, game.players[1].name, 'lucidasanstypewriterregular', 25, placement="midtop"))

# Game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # Registers which action is trying to be performed
        if game.priority == 0 and event.type == pg.KEYDOWN: # if player's turn
            if event.key == pg.K_1:
                game.perform_gameaction(1)
            if event.key == pg.K_2:
                game.perform_gameaction(2)
            if event.key == pg.K_3:
                game.perform_gameaction(3)
            if event.key == pg.K_4:
                game.perform_gameaction(4)
            if event.key == pg.K_5:
                game.perform_gameaction(5)
            if event.key == pg.K_6:
                game.perform_gameaction(26)
    
    if game.priority == 1: # if computer's turn
        # temporary_game = deepcopy(game)
        # temporary_game.is_temporary = True
        # computer_action = computer_ai(temporary_game)
        # game.perform_gameaction(computer_action)
        computer_random(game)

    screen.fill('#E5E4E2') # Light gray background

    # Lines on screen
    pg.draw.line(screen, '#000000', (280, 0), (280, 900), 4) # Left vertical
    pg.draw.line(screen, '#000000', (1280, 0), (1280, 900), 4) # Right vertical
    pg.draw.line(screen, '#000000', (0, 450), (280, 450), 4) # Middle horizontal
    pg.draw.line(screen, '#000000', (280, 740), (1280, 740), 4) # Lower horizontal
    pg.draw.line(screen, '#000000', (280, 160), (1280, 160), 4) # Upper horizontal
    pg.draw.line(screen, '#000000', (1300, 105), (1580, 105), 2) # List of actions underline

    # Dynamic text
    dynamic_text.empty()

    # Updates library counts
    dynamic_text.add(FontSprite(140, 680, str(len(game.players[0].library)), 'lucidasanstypewriter', 40, color='#FFFFFF'))
    dynamic_text.add(FontSprite(140, 220, str(len(game.players[1].library)), 'lucidasanstypewriter', 40, color='#FFFFFF'))
    
    # Updates life totals
    if game.priority == 0:
        dynamic_text.add(FontSprite(140, 520, f"Life: {game.players[0].life_total}", 'lucidasanstypewriter', 50, color='#FF0000'))
        dynamic_text.add(FontSprite(140, 380, f"Life: {game.players[1].life_total}", 'lucidasanstypewriter', 50))
    elif game.priority == 1:
        dynamic_text.add(FontSprite(140, 520, f"Life: {game.players[0].life_total}", 'lucidasanstypewriter', 50))
        dynamic_text.add(FontSprite(140, 380, f"Life: {game.players[1].life_total}", 'lucidasanstypewriter', 50, color='#FF0000'))
    
    # Updates turn information
    if game.turn == 0:
        dynamic_text.add(FontSprite(1440, 550, f"{game.players[0].name}", 'lucidasanstypewriterregular', 40))
    elif game.turn == 1:
        dynamic_text.add(FontSprite(1440, 550, f"{game.players[1].name}", 'lucidasanstypewriterregular', 40))

    # Updates phase information
    dynamic_text.add(FontSprite(1440, 690, game.phase, 'lucidasanstypewriterregular', 40))

    # Updates cards in hand and on field
    cards.empty()
    update_board(game, cards)

    cards.draw(screen)
    library.draw(screen)
    static_text.draw(screen)
    dynamic_text.draw(screen)

    pg.display.flip()
    clock.tick(60)  # Limits FPS to 60

pg.quit()