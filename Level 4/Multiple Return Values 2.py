import pygame
import tsk
pygame.init()


def move_ship(curr_x, curr_image, speed):
    stuff = []
    if curr_image == "RoundShip.png":
        new_x = curr_x - speed
        stuff.append(new_x)
        if new_x <= 0:
            new_image = "RoundShipPurple.png"
            going_left = False
            stuff.append(new_image)
            stuff.append(going_left)
        else:
            new_image = "RoundShip.png"
            going_left = True
            stuff.append(new_image)
            stuff.append(going_left)

    else:
        new_x = curr_x + speed
        stuff.append(new_x)
        if new_x >= 1018:
            new_image = "RoundShip.png"
            going_left = True
            stuff.append(new_image)
            stuff.append(going_left)
        else:
            new_image = "RoundShipPurple.png"
            going_left = False
            stuff.append(new_image)
            stuff.append(going_left)

    return stuff


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
ship = tsk.Sprite("RoundShip.png", 500, 200)
ship.flip_x = True


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    speed = .5 * c.get_time()
    x = move_ship(ship.center_x, ship.image, speed)     
    ship.center_x = x[0]
    ship.image = x[1]
    ship.flip = x[2]

    background.draw()
    ship.draw()

    pygame.display.flip()
    c.tick(30)