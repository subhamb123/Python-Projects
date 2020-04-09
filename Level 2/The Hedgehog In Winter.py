import tsk

import pygame

pygame.init()



window = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)

hedgehog_sheet = tsk.ImageSheet("RocketHedgehog.png", 4, 6)

hedgehog = tsk.Sprite(hedgehog_sheet, 100, 100)

movement_speed = 0.3

trail = []

trail_color = (100, 200, 250)


drawing = True



while drawing:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False



    x, y = hedgehog.center

    if tsk.is_key_down(pygame.K_DOWN):

        y += movement_speed * c.get_time()

    if tsk.is_key_down(pygame.K_UP):

        y -= movement_speed * c.get_time()

    if tsk.is_key_down(pygame.K_RIGHT):

        x += movement_speed * c.get_time()

    if tsk.is_key_down(pygame.K_LEFT):

        x -= movement_speed * c.get_time()

    hedgehog.center = x, y


    trail_point = (int(x - 80), int(y + 100))

    trail.append(trail_point)


    hedgehog.update(c.get_time())

    background.draw()

    for point in trail:

        pygame.draw.circle(window, trail_color, point, 25)

    hedgehog.draw()

    pygame.display.flip()

    c.tick(30)
