import random
import tsk
import pygame
pygame.init()

def make_bubbles(bubbles, speed_tuples):
    number = 0
    old_bubbles = []
    x, y = pygame.mouse.get_pos()

    for sprite in bubbles:
        if sprite.rect.collidepoint(x, y):

            old_bubbles.append(sprite)

            bubb1 = tsk.Sprite("Bubble.png", sprite.x, sprite.y)
            bubb2 = tsk.Sprite("Bubble.png", sprite.center_x, sprite.center_y)

            bubb1.scale = .5 * sprite.scale
            bubb2.scale = bubb1.scale

            bubbles.append(bubb1)
            bubbles.append(bubb2)

            rand_x = random.randint(5, 15) / 100
            rand_y = random.randint(5, 15) / 100

            rand_speed1 = (rand_x, rand_y)
            rand_speed2 = (rand_x * -1, rand_y * -1)

            speed_tuples.append(rand_speed1)
            speed_tuples.append(rand_speed2)

    for bubble_to_remove in old_bubbles:
        number += 1
        curr_index = bubbles.index(bubble_to_remove)
        speed_tuples.remove(speed_tuples[curr_index])
        bubbles.remove(bubble_to_remove)
        
    return number


def move_bubbles(bubbles, speed_tuples, clock):

    for bubble in bubbles:

        curr_index = bubbles.index(bubble)
        x_speed, y_speed = speed_tuples[curr_index]

        bubble.x += x_speed * clock.get_time()
        bubble.y += y_speed * clock.get_time()

        if bubble.center_x > 1018 or bubble.center_x < 0:
            x_speed = x_speed * -1
        if bubble.center_y > 573 or bubble.center_y < 0:
            y_speed = y_speed * -1

        speed_tuples[curr_index] = (x_speed, y_speed)



w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LakeSideView.jpg", 0, 0)
first_bubble = tsk.Sprite("Bubble.png", 500, 100)
first_bubble.scale = 3

bubbles = [first_bubble]
speeds = [(.1, .15)]
splits = 0


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    splits = make_bubbles(bubbles, speeds)                       
    move_bubbles(bubbles, speeds, c)

    background.draw()
    for sprite in bubbles:
        sprite.draw()

    pygame.display.flip()
    c.tick(30)


print("You split " + str(splits) + " bubbles")