import pygame

pygame.init()

window = pygame.display.set_mode([280, 150])


light = (200, 200, 255)

dark = (100, 100, 255)

dark_one = 0


margin = 40

centers = []

for i in range(5):

    point = (margin + i * 50, 75)

    centers.append(point)


drawing = True

while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False



    window.fill((255, 255, 255))


    for i in range(len(centers)):

        if i != dark_one:

            pygame.draw.circle(window, light, centers[i], 15)

        else:

            pygame.draw.circle(window, dark, centers[i], 15)



    dark_one += 1

    dark_one = dark_one % len(centers)


    pygame.display.flip()

    pygame.time.wait(300)
