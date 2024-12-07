import pygame as pg
from Gameobject import *
from LibrarySprite import *

pg.init()
screen = pg.display.set_mode((1600, 900))
clock = pg.time.Clock()
running = True

cards = pg.sprite.Group()
cards.add(Gameobject('Mountain', 'Land', 0))
library = pg.sprite.GroupSingle()
library.add(LibrarySprite())

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONUP:
            cards.update()
    
    screen.fill('#FFFFFF')
    cards.draw(screen)
    library.draw(screen)

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()