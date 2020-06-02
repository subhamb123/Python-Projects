import random
import pygame
pygame.init()


def get_centers():

    x = 100
    y = 100

    coordinates = []

    for i in range(10):

        coordinates.append((x, y))


        x += random.randint(0, 150)
        y += random.randint(0, 50)

        if x > 1000:
            x = 1000
        if y > 550:
            y = 550

    return coordinates


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

coordinates = get_centers()

circles_drawn = 0
timer = 0


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if timer >= 1000:
        timer = 0
        circles_drawn += 1

    w.fill((255, 255, 255))
    for i in range(circles_drawn):
        if i >= 10:
            drawing = False
            break

        pygame.draw.circle(w, (0, 0, 0), coordinates[i], 50, 5)

    pygame.display.flip()
    c.tick(30)
    timer += c.get_time()