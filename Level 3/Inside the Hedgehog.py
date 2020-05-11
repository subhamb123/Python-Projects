import tsk

import pygame

pygame.init()


window = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()

background = tsk.Sprite("HedgehogHouse.jpg", 0, 0)

sleep_sheet = tsk.ImageSheet("HedgehogSleep.png", 5, 6)

brush_sheet = tsk.ImageSheet("HedgehogBrush.png", 5, 6)

run_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)

hedgehog = tsk.Sprite(sleep_sheet, 100, 100)


drawing = True


while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False


    x, y = pygame.mouse.get_pos()

    hedgehog.center = x, y


    if hedgehog.x < 340:

        if hedgehog.image != sleep_sheet:

            print("Sleeping")
            hedgehog.image = sleep_sheet

    elif hedgehog.x < 680:

        if hedgehog.image != brush_sheet:

            print("Brushing")
            hedgehog.image = brush_sheet

    else:

        if hedgehog.image != run_sheet:

            print("Running")
            hedgehog.image = run_sheet


    hedgehog.update(c.get_time())

    background.draw()

    hedgehog.draw()

    pygame.display.flip()

    c.tick(30)
