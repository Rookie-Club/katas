# -*- coding: utf-8 -*-

import pygame
from pygame import *
import sys
from langton import *

white = (255, 255, 255)

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

def dessine_cases_blanches(positions):
    for position in positions:
        rect = (position[0] * 30, position[1] * 30, 30, 30)
        rect_surface = fenetre.subsurface(rect)
        pygame.draw.rect(fenetre, white, rect)

position_fourmi = [2, 3]
orientation_fourmi = [0, -1]
positions_cases_blanches = []

while True:
    pygame.time.wait(3000)

    position_fourmi, orientation_fourmi, positions_cases_blanches = parcours_fourmi(position_fourmi, orientation_fourmi, positions_cases_blanches)
    print "Après ce tour, la fourmi est en " + str(position_fourmi) + ", sont orientation est " + str(orientation_fourmi) + " et les cases blanches doivent être " + str(positions_cases_blanches)

    dessine_cases_blanches(positions_cases_blanches)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
