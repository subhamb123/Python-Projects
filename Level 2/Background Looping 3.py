import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("WinterHills.png", 0, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    
    background.center_x -= 5
    if background.center_x < 0:
        background.center_x = 1018

    background.draw()
    pygame.display.flip()
