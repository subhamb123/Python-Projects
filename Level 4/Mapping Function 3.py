import tsk
import pygame
pygame.init()


def get_name(image):
    if image == "Panda.png":
        return "Panda"
    elif image == "PandaDuck.png":
        return "Panda Duck"
    elif image == "PandaGentleman.png":
        return "Panda Gentleman"
    elif image == "PandaPilot.png":
        return "Panda Pilot"


w = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("LivingRoom.jpg", 0, 0)
panda1 = tsk.Sprite("Panda.png", 600, 0)
panda2 = tsk.Sprite("PandaDuck.png", 100, 0)
panda3 = tsk.Sprite("PandaGentleman.png", 700, 200)
panda4 = tsk.Sprite("PandaPilot.png", 0, 200)

panda1.flip_x = True
panda3.flip_x = True

all_pandas = [panda1, panda2, panda3, panda4]


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            
            for panda in all_pandas:
                if panda.rect.collidepoint(x, y):
                    name = get_name(panda.image)
                    print("You clicked the " + name)

    background.draw()
    for panda in all_pandas:
        panda.draw()

    pygame.display.flip()