import tsk
import pygame
pygame.init()

def water(x, y):
    b = (0, 0, 255)
    pygame.draw.circle(w, b, (465+x, 290+y), 5)
    pygame.draw.circle(w, b, (450+x, 280+y), 5)
    pygame.draw.circle(w, b, (475+x, 310+y), 5)
    pygame.draw.circle(w, b, (490+x, 285+y), 5)
    pygame.draw.circle(w, b, (530+x, 270+y), 5)
    pygame.draw.circle(w, b, (550+x, 290+y), 5)
    pygame.draw.circle(w, b, (475+x, 290+y), 5)
    pygame.draw.circle(w, b, (510+x, 315+y), 5) 
    
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
pug = tsk.Sprite("Pug.png", 0, 0)
pug.center_x = 500
pug.center_y = 300
x = int(pug.center_x)
y = int(pug.center_y)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            pug.center = x, y

    background.draw()
    pug.draw()

    water(x,y)

    pygame.display.flip()
