import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

puffin = tsk.Sprite("PuffinWalk.png", 300, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            puffin.image = "PuffinFly.png" 

        

    window.fill((0, 0, 0))

    puffin.draw()
    pygame.display.flip()
