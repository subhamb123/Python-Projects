import pygame
pygame.init()
window = pygame.display.set_mode([300, 300])
c = pygame.time.Clock()

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

print("Hit all the keys (1-9) as quickly as you can!")

start_time = pygame.time.get_ticks()

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.KEYDOWN:

            if event.key in keys:
                keys.remove(event.key)


            else:
                print("You hit the wrong key!")
                drawing = False



    if len(keys) == 0:
        end_time = pygame.time.get_ticks()
        duration = (end_time - start_time) / 1000
        print("You hit all the keys in " + str(duration) + " seconds.")
        drawing = False

    window.fill((0, 30, 60))
    c.tick(30)
    pygame.display.flip()
