import tsk

import pygame

pygame.init()


def move_towards(sprite, goal, speed):

    goal_x, goal_y = goal


    if goal_x < sprite.center_x - 50:

        sprite.flip_x = True

        sprite.center_x -= speed

    elif goal_x > sprite.center_x + 50:

        sprite.flip_x = False

        sprite.center_x += speed


    if goal_y < sprite.center_y - 10 and sprite.center_y > 120:

        sprite.center_y -= speed

    elif goal_y > sprite.center_y + 10:

        sprite.center_y += speed


w = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()


background = tsk.Sprite("LivingRoom.jpg", 0, 0)

ball = tsk.Sprite("TennisBall.png", 0, 0)

pug = tsk.Sprite("Pug.png", 500, 200)


drawing = True

while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False




    ball.center = pygame.mouse.get_pos()


    speed = .05 * c.get_time()

    move_towards(pug, ball.center, speed)


    background.draw()

    pug.draw()

    ball.draw()


    pygame.display.flip()

    c.tick(30)