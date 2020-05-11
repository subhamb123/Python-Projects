import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("MountainsBackdrop.jpg", 0, 0)
clouds = tsk.Sprite("CloudLayer.png", 0, 450)
panda = tsk.Sprite("PandaDuckSmall.png", 350, -200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    panda.center_y += 0.18 * c.get_time()

    old_center = panda.center
    if pygame.sprite.collide_rect(panda, clouds):
        panda.center = old_center
    background.draw()
    clouds.draw()
    panda.draw()

    pygame.display.flip()
    c.tick(30)
