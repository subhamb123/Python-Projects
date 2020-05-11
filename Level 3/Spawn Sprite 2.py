import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Stage.png", 0, 0)
cat = tsk.Sprite("Cat.png", 434, 320)
note_files = ["Note1.png", "Note2.png", "Note3.png", "Note4.png"]
notes = []

sing_timer = 0
sing_rate = 800

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    sing_timer += c.get_time()
    if sing_timer >= sing_rate:
        sing_timer = 0
        # Spawn a new note here
        for i in note_files:
            note = tsk.Sprite(i, 234, 220)
            notes.append(note)

    for note in notes:
        note.center_y -= 0.3 * c.get_time()

    background.draw()
    cat.draw()
    for note in notes:
        note.draw()

    c.tick(30)
    pygame.display.flip()
