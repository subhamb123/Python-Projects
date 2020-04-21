import tsk

import pygame

pygame.init()


window = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

pug = tsk.Sprite("Pug.png", 300, 300)

dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

dragon = tsk.Sprite(dragon_sheet, 700, 300)

time = 0

speed = 0.1


drawing = True

while drawing:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False


    pug_x, pug_y = pygame.mouse.get_pos()

    pug.center = pug_x, pug_y



    if dragon.center_x < pug_x - 15:

        dragon.center_x += speed * c.get_time()

        dragon.flip_x = False

    elif dragon.center_x > pug_x + 15:

        dragon.center_x -= speed * c.get_time()

        dragon.flip_x = True

    if dragon.center_y < pug_y - 15:

        dragon.center_y += speed * c.get_time()

    elif dragon.center_y > pug_y + 15:

        dragon.center_y -= speed * c.get_time()


    if pygame.sprite.collide_rect(pug, dragon):

        drawing = False


    time += c.get_time()

    speed += c.get_time() / 200000


    dragon.update(c.get_time())

    background.draw()

    dragon.draw()

    pug.draw()

    pygame.display.flip()

    c.tick(30)


print("You lasted " + str(time / 1000) + " seconds.")
