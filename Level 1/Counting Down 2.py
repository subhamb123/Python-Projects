import pygame
pygame.init()
window = pygame.display.set_mode([500, 100])

background_color = (0, 0, 0)
bar_color = (255, 230, 200)

for i in range(10, 0, -1):
    window.fill(background_color)
    rectangle = pygame.Rect(0, 0, i*50, 100)
    pygame.draw.rect(window, bar_color, rectangle)
    pygame.display.flip()
    pygame.time.wait(500)
