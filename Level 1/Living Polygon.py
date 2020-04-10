import pygame

pygame.init()


window = pygame.display.set_mode([400, 400])

window.fill((255,255,255))


points = [(200, 25),(300, 25),(300, 50)]


drawing = True

while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False


    window.fill((255,255,255))

    pygame.draw.polygon(window, ((189,195,223)), points)

    pygame.display.flip()


    x = input("Enter an x coordinate or enter 'quit': ")

    if x == "quit":

        break

    y = input("Enter an y coordinate or enter 'quit': ")

    if y == "quit":

        break


    new_point = (int(x), int(y))

    points.append(new_point)



    print("This is the polygon: " + str(points))

    print()
