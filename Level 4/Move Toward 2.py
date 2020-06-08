import random
import tsk
import pygame
pygame.init()


def move_star(star, ship, speed):
    x = star.center_x
    if ship.center_x < star.center_x:
        x -= speed
    elif ship.center_x > star.center_x:
        x += speed

    y = star.center_y
    if ship.center_y < star.center_y:
        y -= speed
    elif ship.center_y > star.center_y:
        y += speed

    star.center = (x, y)
    return


def move_ship(ship, speed, up):
    if up:
        ship.center_y -= speed

        if ship.center_y <= 0:
            ship.center_y = 0
            return False

    else:
        ship.center_y += speed

        if ship.center_y >= 573:
            ship.center_y = 573
            return True

    return up


def spawn_star(all_stars):
    x = random.choice([0, 982])
    y = random.randint(0, 537)

    star = tsk.Sprite("Star.png", x, y)
    all_stars.append(star)


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("AlienSpace.jpg", 0, 0)
ship = tsk.Sprite("RoundShip.png", 450, 200)

moving_up = True
stars = []
star_timer = 1000

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if star_timer <= 0:
        spawn_star(stars)
        star_timer = 1000

    for star in stars:
        move_star(star, ship, .1 * c.get_time())
    moving_up = move_ship(ship, .3 * c.get_time(), moving_up)

    background.draw()
    ship.draw()
    for star in stars:
        star.draw()

    star_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)