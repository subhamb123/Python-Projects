import tsk
import pygame
pygame.init()
window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("WaterCity.jpg", 0, 0)
helicopter = tsk.Sprite("Helicopter.png", 0, 0)
wall1 = tsk.Sprite("SandWall.png", 300, -250)
wall1.flip_y = not wall1.flip_y
wall1.scale = 0.25
wall2 = tsk.Sprite("SandWall.png", 500, 250)
wall2.scale = 1.25

drawing = True

while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
            
    x, y = pygame.mouse.get_pos()
    helicopter.center = x, y
    if helicopter.center == wall1.center or helicopter.center == wall2.center:
        drawing = False
            
    background.center_x -= 5
    if background.center_x < 0:
        background.center_x = 1018
        
    wall1.center_x -= 5
    if wall1.center_x < 0:
        wall1.center_x = 1018
        
    wall2.center_x -= 5
    if wall2.center_x < 0:
        wall2.center_x = 1018
    
    background.draw()
    helicopter.draw()
    wall1.draw()
    wall2.draw()
    pygame.display.flip()
