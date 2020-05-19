import tsk
import pygame
pygame.init()

def draw_ships(num_ships):
    if num_ships <= 0:
        return

    draw_increment = 1018 / num_ships
    x = 0
    y = 200

    for i in range(num_ships):
        ship = tsk.Sprite("RoundShip.png", x, y)
        ship.draw()
        x += draw_increment


w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("AlienSpace.jpg", 0, 0)
ships = int(input("How many ships should there be? "))

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    draw_ships(ships)
    pygame.display.flip()
