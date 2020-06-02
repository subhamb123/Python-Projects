import tsk
import random
import pygame
pygame.init()


def get_bug_name(num):
    if num == 1:
        return "Bee.png"
    else:
        return "Butterfly.png"


def get_bug_dir(num):
    if num == 1:
        return True
    else:
        return False


w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)

all_bugs = []
for i in range(random.randint(3, 15)):

    random_bug = random.randint(1, 2)

    random_direction = random.randint(1, 2)
    bug_dir = get_bug_dir(random_direction)


    bug = tsk.Sprite(get_bug_name(random_bug), random.randint(0, 900), random.randint(0, 500))
    bug.flip_x = bug_dir
    all_bugs.append(bug)


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    for bug in all_bugs:
        bug.draw()
    pygame.display.flip()