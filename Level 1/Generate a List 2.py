import pygame
import random
pygame.init()
window = pygame.display.set_mode([500, 500])
height = 400
size = 100

circles = []

for i in range(8):
    num = random.randint(0, 500)
    circles.append(num)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    height -= 5
    size -= 1

    if size <= 0:
        break

    color = (90, 120, 255)
    window.fill((0, 0, 30))
    water = pygame.Rect(0, 300, 500, 200)
    pygame.draw.rect(window, (90, 120, 255), water)

    for circle in circles:
        pygame.draw.circle(window, (140, 170, 255), (circle, height), size)

    pygame.display.flip()
