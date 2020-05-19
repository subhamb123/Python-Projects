import random
import pygame
pygame.init()

def draw_diamond(window, x, y):
    pt1 = (-100+x, 0+y)
    pt2 = (-75+x, 30+y)
    pt3 = (-50+x, 0+y)
    pt4 = (-75+x, -30+y)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3, pt4])


def draw_heart(window, x, y):
    pt1 = (100+x, 0+y)
    pt2 = (50+x, 0+y)
    pt3 = (75+x, 30+y)
    circle_left = (62+x, -5+y)
    circle_right = (88+x, -5+y)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (255, 0, 0), (circle_left), 14)
    pygame.draw.circle(window, (255, 0, 0), (circle_right), 14)


def draw_club(window, x, y):
    pt1 = (-21+x, 97+y)
    pt2 = (21+x, 97+y)
    pt3 = (0+x, 77+y)
    circle_left = (-14+x, 70+y)
    circle_right = (14+x, 70+y)
    circle_top = (0+x, 50+y)
    pygame.draw.polygon(window, (0, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (0, 0, 0), (circle_left), 16)
    pygame.draw.circle(window, (0, 0, 0), (circle_right), 16)
    pygame.draw.circle(window, (0, 0, 0), (circle_top), 16)


def draw_spade(window, x, y):
    pt1 = (-21+x, -45+y)
    pt2 = (21+x, -45+y)
    pt3 = (0+x, -65+y)
    pt4 = (-29+x, -75+y)
    pt5 = (29+x, -75+y)
    pt6 = (0+x, -110+y)
    circle_left = (-14+x, -70+y)
    circle_right = (14+x, -70+y)
    pygame.draw.polygon(window, (0, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (0, 0, 0), (circle_left), 16)
    pygame.draw.circle(window, (0, 0, 0), (circle_right), 16)
    pygame.draw.polygon(window, (0, 0, 0), [pt4, pt5, pt6])


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
timer = 2000
x = 500
y = 250

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if timer <= 0:
        timer = 2000
        x = random.randint(100, 900)
        y = random.randint(100, 450)

    w.fill((255, 255, 255))

    draw_diamond(w, x, y)                                     
    draw_heart(w, x, y)
    draw_club(w, x, y)
    draw_spade(w, x, y)

    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)
