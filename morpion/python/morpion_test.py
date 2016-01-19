import pygame
from pygame.locals import *

screen = pygame.display.set_mode((480, 480))

#ligne_1 / case_1 = [0, 160, 0, 160] / case_2 = [160, 320, 0, 160] / case_3 = [320, 480, 0, 160]
#ligne_2 / case_1 = [0, 160, 160, 320] / case_2 [160, 320, 160, 320] / case_3 = [320, 480, 160, 320]
#ligne_3 / case_1 = [0, 160, 320, 480] / case_2 [160, 320, 320, 480] / case_3 = [320, 480, 320, 480]

def dessine_croix():
    pygame.draw.line(screen, 0x0000a0, [0, 0], [300,300], 10)
    pygame.draw.line(screen, 0x0000a0, [300, 0], [0,300], 10)

def dessine_rond():
    pygame.draw.circle(screen, 0xa00000, [240, 240], 200, 10)

#choisir aleatoirement un chiffre entre 1 et 2 pour commencer la partie

#etat_courant = None
player = 1

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if player == 1:
            #etat_courant == "rond":
                screen.fill((0,0,0))
                dessine_croix()
                #etat_courant = "croix"
                player = 2
            else:
                screen.fill((0,0,0))
                dessine_rond()
                #etat_courant = "rond"
                player = 1
    pygame.display.flip()
    pygame.time.delay(100)
