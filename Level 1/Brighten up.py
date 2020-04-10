import random

import pygame

pygame.init()


window = pygame.display.set_mode([500, 500])

window.fill((0,0,0))


max_circles = random.randint(20,50)

color_increment = int(255/max_circles)


for i in range(max_circles):


    color = (i*color_increment, i*color_increment, i*color_increment)

    size = i*5

    point = (random.randint(25,475), random.randint(25,475))



    pygame.draw.circle(window, color, point, size)

    pygame.display.flip()

    pygame.time.wait(200)
