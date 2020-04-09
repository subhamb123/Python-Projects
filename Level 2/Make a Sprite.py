import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("OutdoorBushScene.jpg", 0, 0)


drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    background.draw()
    pygame.display.flip()
