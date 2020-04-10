import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])
background_color = (20, 30, 60)


circle_color = (120, 130, 160)
centers = []
sizes = []


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.mouse.get_pos()
            centers.append(center)
            sizes.append(100)


    for i in range(len(sizes)):
        sizes[i] -= 1


    window.fill(background_color)

    for i in range(len(centers)):
        if(sizes[i] > 0):
            pygame.draw.circle(window, circle_color, centers[i], sizes[i])


    pygame.display.flip()
