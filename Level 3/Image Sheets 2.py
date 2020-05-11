import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(sheet, 400, 100)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    ship.update(c.get_time())
    ship.draw()


    c.tick(30)
    pygame.display.flip()
