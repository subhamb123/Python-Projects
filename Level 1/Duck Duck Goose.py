import random
import pygame
pygame.init()


animals = ["duck", "duck", "duck", "duck", "duck", "goose"]

selected = "duck"


while selected != "goose":


    random_num = random.randint(0, len(animals)-1)
    selected = animals[random_num]


    pygame.time.wait(1500)


    if selected == "duck":
        print("Duck...")
    else:
        print("Goose!")
