import pygame
pygame.init()

for i in range(10, 0, -1):
    print("New year in " + str(i) + " seconds.")
    pygame.time.wait(1000)

print("\o/ Happy New Year! \o/")
