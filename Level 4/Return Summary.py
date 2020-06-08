import tsk
import random
import pygame
pygame.init()


def make_stars(all_stars):
    num_stars = random.randint(1, 20)

    for i in range(num_stars):
        x = random.randint(0, 990)
        y = random.randint(0, 540)
        star = tsk.Sprite("Star.png", x, y)
        all_stars.append(star)
        return num_stars



w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
ship_sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(ship_sheet, 760, 280)
ship_speed = 30
timer = 1000
stars = []


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            ship_speed += make_stars(stars)

    if timer <= 0:
        ship_speed -= 3
        timer = 1000

    if ship_speed <= 0:
        ship_speed = 0

    ship.image_animation_rate = ship_speed

    background.draw()
    for star in stars:
        star.draw()
    ship.draw()
    ship.update(c.get_time())

    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)