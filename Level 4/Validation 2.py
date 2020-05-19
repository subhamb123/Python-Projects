import pygame
pygame.init()

def draw_grid(num_squares, square_size):
    if num_squares < 1:
        print("Error, 8 will be used as default.")
        num_squares = 8
    elif num_squares > 10:
        print("Error, 8 will be used as default.")
        num_squares = 8
    if square_size != 100:
        return

    w = pygame.display.set_mode([num_squares * 100, num_squares * 100])
    w.fill((255, 255, 255))

    for i in range(num_squares):
        for j in range(num_squares):
            if (i % 2) == 0:
                if (j % 2) == 0:
                    square = pygame.Rect(i * square_size, j * square_size, square_size, square_size)
                    pygame.draw.rect(w, (0, 0, 0), square)
            else:
                if (j % 2) == 1:
                    square = pygame.Rect(i * square_size, j * square_size, square_size, square_size)
                    pygame.draw.rect(w, (0, 0, 0), square)


squares = int(input("How big is your board (1 - 10)? "))
draw_grid(squares, 100)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    pygame.display.flip()