import tsk

import pygame

pygame.init()


window = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()


background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

wiz_sheet = tsk.ImageSheet("WizardWalking.png", 4, 6)

wizard = tsk.Sprite(wiz_sheet, 150, 280)

dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

dragon = tsk.Sprite(dragon_sheet, 650, 30)

wizard.image_animation_rate = 30

appearing = False

dragon_timer = 0

appear_time = 2000

hide_time = 3000


drawing = True

while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False


    dragon_timer += c.get_time()

    if appearing and dragon_timer > appear_time:

        dragon_timer = 0

        appearing = False

    if not appearing and dragon_timer > hide_time:

        dragon_timer = 0

        appearing = True


    if not appearing:

        if tsk.get_key_pressed(pygame.K_RIGHT):

            wizard.x += .1 * c.get_time()

            wizard.flip_x = False

        if tsk.get_key_pressed(pygame.K_LEFT):

            wizard.x -= .1 * c.get_time()

            wizard.flip_x = True


    if appearing:

        wizard.image_animation_rate = 0

    else:

        wizard.image_animation_rate = 30

    dragon.update(c.get_time())

    wizard.update(c.get_time())


    background.draw()

    if appearing:

        dragon.draw()

    wizard.draw()

    pygame.display.flip()

    c.tick(30)
    
