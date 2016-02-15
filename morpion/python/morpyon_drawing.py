import pygame

def croix(cell_surface):
    pygame.draw.line(cell_surface, 0x0000a0, [0, 0], [213, 133], 10)
    pygame.draw.line(cell_surface, 0x0000a0, [213, 0], [0, 133], 10)

def rond(cell_surface):
    pygame.draw.circle(cell_surface, 0x00000, [107, 66], 100, 10)

def grille(screen):
    pygame.draw.line(screen, 0x0000a0, [300, 0], [300, 900], 10)
    pygame.draw.line(screen, 0x0000a0, [600, 0], [600, 900], 10)
    pygame.draw.line(screen, 0x0000a0, [0, 300], [900, 300], 10)
    pygame.draw.line(screen, 0x0000a0, [0, 600], [900, 600], 10)
