import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])

sky = tsk.Sprite("outdoor_sky.png", 0, 0)
back_mountains = tsk.Sprite("outdoor_mountain_b.png", 0, 0)
front_mountains = tsk.Sprite("outdoor_mountain_a.png", 0, 0)
foreground = tsk.Sprite("outdoor_foreground.png", 0, 0)



drawing = True
while drawing:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    sky.draw()
    back_mountains.draw()
    front_mountains.draw()
    foreground.draw()
    

    pygame.display.flip()
