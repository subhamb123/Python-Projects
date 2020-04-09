import tsk

import pygame

pygame.init()


window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("space_background.jpg", 0, 0)

galaxies = tsk.Sprite("galaxies_scrolling.png", 0, 0)

stars = tsk.Sprite("stars_scrolling.png", 0, 0)

asteroids = tsk.Sprite("asteroids_scrolling.png", 0, 0)

galaxies_speed = -1

stars_speed = -2

asteroids_speed = -7


drawing = True


while drawing:


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            drawing = False



    if galaxies.center_x < 0:

        galaxies.center_x = 1900

    galaxies.center_x += galaxies_speed


    if stars.center_x < 0:

        stars.center_x = 3025

    stars.center_x += stars_speed


    if asteroids.center_x < 0:

        asteroids.center_x = 2400

    asteroids.center_x += asteroids_speed


    background.draw()

    stars.draw()

    galaxies.draw()

    asteroids.draw()

    pygame.display.flip()
