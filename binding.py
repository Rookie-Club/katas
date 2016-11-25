import pygame
from pygame import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

continuer = int(input())

pygame.display.flip()

rect = pygame.Rect(10, 20, 30, 30)



while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
