import tsk
import random
import pygame
pygame.init()


def draw_arrow(window, direction, color):


    if direction == "left" or direction == "right":

        body_rect = pygame.Rect(600, 200, 200, 100)

    else:

        body_rect = pygame.Rect(600, 200, 100, 200)


    if direction == "left":

        far = (450, 250)

        base1 = (600, 150)

        base2 = (600, 350)

    elif direction == "right":

        far = (950, 250)

        base1 = (800, 150)

        base2 = (800, 350)

    elif direction == "up":

        far = (650, 50)

        base1 = (550, 200)

        base2 = (750, 200)

    elif direction == "down":

        far = (650, 550)

        base1 = (550, 400)

        base2 = (750, 400)


    if color == "green":

        draw_color = (0, 255, 0)

    elif color == "red":

        draw_color = (255, 0, 0)


    pygame.draw.rect(window, draw_color, body_rect)

    pygame.draw.polygon(window, draw_color, [far, base1, base2])


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("ScienceLab.jpg", 0, 0)
robot = tsk.Sprite("RobotDance.png", 100, 150)

arrow = "left"
arrow_color = "red"
arrow_timer = 0
arrow_limit = 1000
directions = ["left", "right", "up", "down"]

score = 0
mistakes = 0


drawing = True
while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            drawing = False


        if event.type == pygame.KEYDOWN:

            if tsk.get_key_pressed(pygame.K_RIGHT) and arrow == "right" or tsk.get_key_pressed(pygame.K_LEFT) and arrow == "left" or tsk.get_key_pressed(pygame.K_DOWN) and arrow == "down" or tsk.get_key_pressed(pygame.K_UP) and arrow == "up":

                arrow_color = "green"

                score += 1

            else:

                mistakes += 1


    if arrow_timer >= arrow_limit:



        if arrow_color == "red":

            mistakes += 1


        rand_arrow = random.randint(0, 3)

        arrow = directions[rand_arrow]


        arrow_color = "red"


        arrow_timer = 0

        if arrow_limit > 500:

            arrow_limit -= 10



    background.draw()
    robot.draw()

    draw_arrow(w, arrow, arrow_color)


    arrow_timer += c.get_time()

    pygame.display.flip()
    c.tick(30)

    if mistakes >= 5:

        drawing = False


print("Your final score was: " + str(score))