import random
import tsk
import pygame
pygame.init()


def new_sprite(all_sprites, image = "SmallBrownRock.png"):                     
    x = random.randint(20, 950)
    y = random.randint(100, 400)
    sprite = tsk.Sprite(image, x, y)
    all_sprites.append(sprite)


def find_rock(all_sprites):
    for sprite in all_sprites:
        if sprite.image == "SmallBrownRock.png":
            return sprite

    return -1


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
sprite_list = [background]
possible_keys = [pygame.K_x, pygame.K_t, pygame.K_b, pygame.K_q, pygame.K_w, pygame.K_z, pygame.K_y, pygame.K_l]
hidden_key = random.choice(possible_keys)
remove_rock_timer = 2000

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN:

            if event.key == hidden_key:
                new_sprite(sprite_list, "RoundGemBlue.png")
                hidden_key = random.choice(possible_keys)

            else:
                new_sprite(sprite_list, "SmallBrownRock.png") 

    if remove_rock_timer <= 0:
        remove_rock_timer = 2000
        first_rock = find_rock(sprite_list)
        if first_rock != -1:
            sprite_list.remove(first_rock)

    for sprite in sprite_list:
        sprite.draw()

    remove_rock_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)