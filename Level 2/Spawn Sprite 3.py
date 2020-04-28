import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
up_sparkles = []
down_sparkles = []
sparkles_per_firework = 8

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(sparkles_per_firework):
                x, y = pygame.mouse.get_pos()
                sparkle1 = tsk.Sprite("Star.png", x, y)
                sparkle2 = tsk.Sprite("Star.png", x, y)
                up_sparkles.append(sparkle1)
                down_sparkles.append(sparkle2)

    for sparkle in up_sparkles:
        sparkle.center_y -= 0.2 * c.get_time()
        sparkle.center_x += 0.02 * random.randint(-20, 20) * c.get_time()
    for sparkle in down_sparkles:
        sparkle.center_y += 0.2 * c.get_time()
        sparkle.center_x += 0.02 * random.randint(-20, 20) * c.get_time()

    background.draw()
    for sparkle in up_sparkles:
        sparkle.draw()
    for sparkle in down_sparkles:
        sparkle.draw()

    c.tick(30)
    pygame.display.flip()
