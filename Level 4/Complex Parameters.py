import random
import tsk
import pygame
pygame.init()


def random_background(background, flip = False):
    if flip:
        background.flip_y = True
    images = ["AlienSpace.jpg", "Hills.jpg", "SchoolHallway.jpg"]
    back = random.choice(images)
    background.image = back
    return back

w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Hills.jpg", 0, 0)

panda = tsk.Sprite("Panda.png", 100, 100)
rock = tsk.Sprite("BigMossyRock.png", 400, 20)
vase = tsk.Sprite("ShortVase.png", 670, 280)


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            back = random_background(background, True)
            print("The new backgound is: " + back)


    background.draw()
    rock.draw()
    panda.draw()
    vase.draw()
    pygame.display.flip()