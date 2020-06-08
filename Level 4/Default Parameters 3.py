import tsk
import pygame
pygame.init()


def spin_ball(ball, clock, ball_speed = 0.1):                 
    speed = ball_speed * clock.get_time()
    ball.angle -= speed

w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Arena.jpg", 0, 0)
soccer_ball = tsk.Sprite("SoccerBall.png", 160, 250)
tennis_ball = tsk.Sprite("TennisBall.png", 460, 350)
other_ball = tsk.Sprite("Ball.png", 760, 250)


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
 
    spin_ball(soccer_ball, c, .1)                       
    spin_ball(other_ball, c, .1)                        

    if tsk.is_key_down(pygame.K_SPACE):
        spin_ball(tennis_ball, c, .5)
    else:
        spin_ball(tennis_ball, c)                   

    background.draw()
    soccer_ball.draw()
    tennis_ball.draw()
    other_ball.draw()

    pygame.display.flip()
    c.tick(30)