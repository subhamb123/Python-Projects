import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

cat = tsk.Sprite("Cat.png", 100, 100)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    window.fill((0, 0, 0))
    
    cat.draw()

    pygame.display.flip()
