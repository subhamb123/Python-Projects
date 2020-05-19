import random
import pygame
pygame.init()


def draw_head(window, x, y):
    pygame.draw.circle(window, (0, 0, 0), (x, y), 75)
    pygame.draw.circle(window, (0, 200, 0), (x, y), 72)

    draw_scales(x, y, window)

    pygame.draw.circle(window, (0, 0, 0), (x, y + 20), 15)
    pygame.draw.circle(window, (0, 0, 0), (x, y - 20), 15)
    pygame.draw.line(window, (250, 50, 50), (x + 75, y), (x + 95, y), 7)
    pygame.draw.line(window, (250, 50, 50), (x + 95, y), (x + 115, y + 15), 7)
    pygame.draw.line(window, (250, 50, 50), (x + 95, y), (x + 115, y - 15), 7)


def draw_body_segment(window, x, y):
    pygame.draw.circle(window, (0, 0, 0), (x, y), 75)
    pygame.draw.circle(window, (0, 200, 0), (x, y), 72)

    draw_scales(x, y, window)


def draw_scales(x, y, window):
    for i in range(4):
        scale_x = random.randint(x - 45, x + 45)
        scale_y = random.randint(y - 40, y + 60)
        pygame.draw.line(window, (100, 255, 100), (scale_x, scale_y), (scale_x - 10, scale_y - 10))
        pygame.draw.line(window, (100, 255, 100), (scale_x, scale_y), (scale_x + 10, scale_y - 10))


w = pygame.display.set_mode([1018, 573])
w.fill((255, 255, 255))
c = pygame.time.Clock()
timer = 500
start_x = random.randint(250, 950)
start_y = random.randint(50, 500)

draw_head(w, start_x, start_y)
draw_body_segment(w, start_x - 145, start_y)
body_x = start_x - 145
body_y = start_y


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            body_x = random.randint(body_x - 70, body_x + 70)
            body_y = random.randint(body_y - 70, body_y + 70)
            draw_body_segment(w, body_x, body_y)

    pygame.display.flip()
    c.tick(30)
