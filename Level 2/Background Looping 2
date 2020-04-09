import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

space = tsk.Sprite("Space.jpg", 0, 0)
asteroids = tsk.Sprite("AsteroidsScrolling.png", 0, 150)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    asteroids.center_x -= 8
    if asteroids.center_x < 0:
        asteroids.center_x = 1018



    space.draw()
    asteroids.draw()
    pygame.display.flip()
