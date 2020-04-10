import pygame
pygame.init()

x_positions = []
y_positions = []

x_pos = 0
y_pos = 0
while True:
    x_pos = input("Enter x-position (Enter 'done' to exit)")
    if x_pos == "done":
        break
    x_positions.append(x_pos)
    y_pos = input("Enter y-position")
    y_positions.append(y_pos)

window = pygame.display.set_mode([500, 500])
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    index = 1
    while index < len(x_positions):
        p1 = (int(x_positions[index]), int(y_positions[index]))
        p2 = (int(x_positions[index - 1]), int(y_positions[index - 1]))
        pygame.draw.line(window, (0, 0, 0), p1, p2, 5)
        index += 1

    pygame.display.flip()
