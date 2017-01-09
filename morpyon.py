#! /usr/bin/env python

from sys import exit
import pygame
from pygame.locals import *
from morpyon_game import *
import morpyon_drawing

screen_size = (900, 900)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (64, 64, 64)
position = (10, 10)

screen = pygame.display.set_mode(screen_size)

screen.fill(grey)

game = MorpyonGame((screen_size))

for (x,y) in game.positions():
    cell = pygame.Rect((x,y), game.box_size())
    cell_surface = screen.subsurface(cell)
    cell_surface.fill(red)
    morpyon_drawing.grille(screen)

etat_courant = "vide"
player = 1

def croix():
    pygame.draw.line(cell_surface, 0x0000a0, [0, 0], [213, 133], 10)
    pygame.draw.line(cell_surface, 0x0000a0, [213, 0], [0, 133], 10)

def rond():
    pygame.draw.circle(cell_surface, 0x00000, [107, 66], 100, 10)


while 1:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if etat_courant != "vide":
                if player == 1:
                    croix()
                    player = 2
                else:
                    rond()
                    player = 1
            etat_courant = "plein"
        if event.type == QUIT:
            exit()
    pygame.display.flip()
    pygame.time.delay(100)



