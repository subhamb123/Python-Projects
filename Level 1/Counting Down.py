import pygame
pygame.init()

for i in range(5, 0, -1):
    distance = 100*i
    print("In " + str(distance) + " feet, take a left.")
    pygame.time.wait(1000)

print("Turn left now.")
