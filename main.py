import pygame as pg
from Gameobject import *
from sprites import *

# Pygame standard setup
pg.init()
screen = pg.display.set_mode((1600, 900))
clock = pg.time.Clock()
running = True

# Fonts
font_regular40 = pg.font.SysFont('lucidasanstypewriterregular', 40)
font_regular30 = pg.font.SysFont('lucidasanstypewriterregular', 30)
font_bold40 = pg.font.SysFont('lucidasanstypewriter', 40)

# Sprites
cards = pg.sprite.Group()
# cards.add(Gameobject('Mountain', 'Land', 0))

# Library card backs
library = pg.sprite.Group()
library.add(LibrarySprite(140, 125))
library.add(LibrarySprite(140, 775))

static_text = pg.sprite.Group()
static_text.add(FontSprite(1440, 30, 'List of', font_bold40))
static_text.add(FontSprite(1440, 75, 'Game Actions', font_bold40))
static_text.add(FontSprite(1290, 150, '1: Pass Priority', font_regular30, placement="left"))
static_text.add(FontSprite(1290, 200, '2: Play Mountain', font_regular30, placement="left"))
static_text.add(FontSprite(1290, 250, '3: Play Creature', font_regular30, placement="left"))
static_text.add(FontSprite(1290, 300, '4: Play Bolt', font_regular30, placement="left"))
static_text.add(FontSprite(1290, 350, '5: Attack All', font_regular30, placement="left"))

dynamic_text = pg.sprite.Group()

library_list = [0, 1, 2, 3, 4, 5]

# Game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # Registers which action is trying to be performed
        if event.type == pg.KEYDOWN and event.key == pg.K_1:
            print('1')
            library_list.append(0)
            dynamic_text.empty()
        if event.type == pg.KEYDOWN and event.key == pg.K_2:
            print('2')
        if event.type == pg.KEYDOWN and event.key == pg.K_3:
            print('3')
        if event.type == pg.KEYDOWN and event.key == pg.K_4:
            print('4')
        if event.type == pg.KEYDOWN and event.key == pg.K_5:
            print('5')
    
    screen.fill('#E5E4E2') # Makes the screen gray

    # Lines on screen
    pg.draw.line(screen, '#000000', (280, 0), (280, 900), 4)
    pg.draw.line(screen, '#000000', (1280, 0), (1280, 900), 4)
    pg.draw.line(screen, '#000000', (0, 450), (280, 450), 4)
    pg.draw.line(screen, '#000000', (280, 750), (1280, 750), 4)
    pg.draw.line(screen, '#000000', (280, 150), (1280, 150), 4)
    pg.draw.line(screen, '#000000', (1300, 105), (1580, 105), 2)

    # Dynamic text
    dynamic_text.add(FontSprite(140, 125, str(len(library_list)), font_bold40, color='#FFFFFF'))
    dynamic_text.add(FontSprite(140, 775, str(len(library_list)), font_bold40, color='#FFFFFF'))

    # cards.draw(screen)
    library.draw(screen)
    static_text.draw(screen)
    dynamic_text.draw(screen)

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()