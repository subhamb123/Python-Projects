import pygame
pygame.init()

def circles(window, corner, flag):                            
    
    if corner == 1:
        x = 100
        y = 100
        modify_x = 100
        modify_y = 100

    elif corner == 2:
        x = 400
        y = 100
        modify_x = -100
        modify_y = 100

    elif corner == 3:
        x = 400
        y = 400
        modify_x = -100
        modify_y = -100

    elif corner == 4:
        x = 100
        y = 400
        modify_x = 100
        modify_y = -100

    size = 120
    for i in range(5):

        if flag:
            pygame.draw.circle(window, (0, 0, 255), (x, y), size, 3)
        else:
            pygame.draw.circle(window, (0, 0, 255), (x, y), size)

        x += modify_x
        y += modify_y
        size -= 20


w = pygame.display.set_mode([500, 500])

start_val = 100
flag = True
start = 0

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    w.fill((0, 0, 0))

    circles(w, start + 1, flag)                               

    flag = not flag
    start = ((start + 1) % 4)

    pygame.display.flip()
    pygame.time.wait(1000)
