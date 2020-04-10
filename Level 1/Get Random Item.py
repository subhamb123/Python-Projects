import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 100])
c = pygame.time.Clock()
positions = [10, 20, 40, 80, 160, 320]
star_rect = pygame.Rect(10, 40, 20, 20)

timer = 0
flip_time = 200

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer >= flip_time:
        timer = 0

        choice = random.randint(0, len(positions)-1)
        star_rect.x = positions[choice]



    window.fill((20, 20, 45))
    pygame.draw.ellipse(window, (230, 210, 170), star_rect)
    pygame.draw.ellipse(window, (250, 230, 190), star_rect, 3)

    pygame.display.flip()
    c.tick()
