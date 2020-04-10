import pygame
import random
pygame.init()
window = pygame.display.set_mode([300, 300])
color = 255
c = pygame.time.Clock()

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

print("Can you guess the right key (1-9?)")

number = random.randint(0, len(keys)-1)
answer = keys[number]

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.KEYDOWN:

            if event.key == answer:
                print("You guessed it correctly!")
                drawing = False


            color -= 25
            if color < 0:
                color = 0

    window.fill((0, color, 60))
    pygame.draw.circle(window, (255-color, 0, 0), (150, 150), 50)

    pygame.display.flip()
    c.tick()
