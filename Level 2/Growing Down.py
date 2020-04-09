import tsk

import pygame

pygame.init()


window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("science_lab.jpg", 0, 0)

panda = tsk.Sprite("panda.png", 0, 0)

panda.center = (509, 250)


drawing = True


while drawing:


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            drawing = False


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:

            panda.center_x -=20

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:

            panda.center_x +=20

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

            panda.scale -= 0.05

            panda.center_y +=10


    if panda.scale < 0.1:

        panda.scale = 0.1


    background.draw()

    panda.draw()

    pygame.display.flip()
