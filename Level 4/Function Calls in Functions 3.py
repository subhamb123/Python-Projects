import tsk
import pygame
pygame.init()


def draw_line(window, x, y):
    pygame.draw.line(window, (0, 0, 0), (x, y), (x, y + 50), 5)


def draw_square(window, x, y):
    start_x = x - 25
    start_y = y - 25
    r = pygame.Rect(start_x, start_y, 50, 50)

    g = int((x / 1018) * 255)
    if g > 255:
        g = 255
    color = (0, g, 0)
    pygame.draw.rect(window, color, r)


def draw_circle(window, x, y):
    b = int((x / 1018) * 255)
    if b > 255:
        b = 255
    color = (0, 0, b)
    pygame.draw.circle(window, color, (x, y), 25)


def draw_triangle(window, x, y):
    p1 = (x - 25, y + 25)
    p2 = (x, y - 25)
    p3 = (x + 25, y + 25)

    r = int((x / 1018) * 255)
    if r > 255:
        r = 255
    color = (r, 0, 0)
    pygame.draw.polygon(window, color, [p1, p2, p3])


def draw_shapes(s, c, t, window, position):
    if position > 1100 or position < -100:
        return

    draw_line(window, position, 0)
    draw_line(window, position, 350)
    if s:
        draw_square(window, position, 100)
    if c:
        draw_circle(window, position, 200)
    if t:
        draw_triangle(window, position, 300)

w = pygame.display.set_mode([1000, 400])
w.fill((255, 255, 255))
c = pygame.time.Clock()
timer = 0


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if tsk.is_key_down(pygame.K_SPACE):
        timer += c.get_time()
    else:
        timer = 0

    circle = False
    square = False
    triangle = False

    if tsk.is_key_down(pygame.K_a):
        circle = True
    if tsk.is_key_down(pygame.K_s):
        square = True
    if tsk.is_key_down(pygame.K_d):
        triangle = True

    w.fill((180, 180, 180))
    if timer > 0:
        draw_shapes(circle, square, triangle, w, int(timer / 5))

    pygame.display.flip()
    c.tick(30)
