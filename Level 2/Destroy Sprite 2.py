import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("ScienceLab.jpg", 0, 0)
robot = tsk.Sprite("FireBot.png", 0, 0)
fires = []

for i in range(100):
    x = random.randint(0, 852)
    y = random.randint(0, 369)
    file = random.choice(["SmallFire.png", "SmallFire2.png"])
    fire = tsk.Sprite(file, x, y)
    fires.append(fire)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    robot.center = x, y

    destroy = []
    for fire in fires:
        if pygame.sprite.collide_rect(fire, robot):
            destroy.append(fire)
    for fire in destroy:
        fires.remove(fire)


    background.draw()
    for fire in fires:
        fire.draw()
    robot.draw()

    pygame.display.flip()
    c.tick(30)
