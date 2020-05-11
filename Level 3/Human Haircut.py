import tsk

import pygame

pygame.init()

c = pygame.time.Clock()


window = pygame.display.set_mode([1018, 573])

window.fill((255,255,255))

robot = tsk.Sprite("robot_bust.png", 0, 0)

robot.draw()


hair_color = (0,0,0)

drawing = False


done = False


while not done:

    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            

            done = True


        elif event.type == pygame.MOUSEBUTTONDOWN:

            drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:

            drawing = False


    x, y = pygame.mouse.get_pos()

    if drawing:

        pygame.draw.circle(window, hair_color, (x,y), 10)

    c.tick(30)

    pygame.display.flip()
