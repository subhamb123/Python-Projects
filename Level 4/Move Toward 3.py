import tsk
import pygame
pygame.init()


def move_to_mouse(sprite, speed):

    x, y = pygame.mouse.get_pos()
    sprite_x = sprite.center_x
    sprite_y = sprite.center_y

    if x < sprite_x:
        sprite_x -= speed
    elif x > sprite_x:
        sprite_x += speed

    if y < sprite_y:
        sprite_y -= speed
    elif y > sprite_y:
        sprite_y += speed

    sprite.center = sprite_x, sprite_y
    return



def spawn_ghost(all_ghosts):
    ghost = tsk.Sprite("Ghost.png", 0, 0)
    ghost.center = (100, 250)
    all_ghosts.append(ghost)


w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("HauntedForest.jpg", 0, 0)
tower = tsk.Sprite("SkullTower.png", -100, 150)
ghosts = []

ghost_timer = 1000

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if ghost_timer <= 0:
        spawn_ghost(ghosts)
        ghost_timer = 5000

    for ghost in ghosts:
        move_to_mouse(ghost, .08 * c.get_time())

    background.draw()
    tower.draw()
    for ghost in ghosts:
        ghost.draw()

    ghost_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)