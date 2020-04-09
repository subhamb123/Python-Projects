import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

meadow = tsk.Sprite("OutdoorBushes.jpg", 0, 0)

# Hedgehog should use an ImageSheet
sheet = tsk.ImageSheet("HedgehogSleep.png", 5, 6)
hedgehog = tsk.Sprite(sheet, 500, 250)    

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    meadow.draw()
    hedgehog.update(c.get_time())
    hedgehog.draw()

    # Update animation

    c.tick(30)
    pygame.display.flip()
