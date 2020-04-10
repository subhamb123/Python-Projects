import pygame
import random
pygame.init()

window = pygame.display.set_mode([800, 600])
c = pygame.time.Clock()
x_positions = []
y_positions = []

timer = 0
star_time = 40

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer >= star_time:
        timer = 0

        x_positions.append(0)

        number = random.randint(0,600)
        y_positions.append(number)


    window.fill((5, 0, 43))
    index = 0
    while index < len(x_positions):
        x_positions[index] += 1
        pygame.draw.circle(window, (250, 250, 230), (x_positions[index], y_positions[index]), 3)
        index += 1

    pygame.display.flip()
    c.tick()
