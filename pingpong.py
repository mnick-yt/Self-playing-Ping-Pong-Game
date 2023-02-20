import pygame
import random

# initialize Pygame
pygame.init()

# set the window size
win_width = 1280
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Ping Pong")

# set the game variables
ball_radius = 10
ball_x = int(win_width / 2)
ball_y = int(win_height / 2)
ball_color = (0, 255, 0)
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = 5 * random.choice([-1, 1])

paddle_width = 10
paddle_height = 80
paddle_color = (255, 0, 0)
paddle_speed = 7

left_paddle_x = 50
left_paddle_y = int(win_height / 2) - int(paddle_height / 2)

right_paddle_x = win_width - 50 - paddle_width
right_paddle_y = int(win_height / 2) - int(paddle_height / 2)

score_font = pygame.font.SysFont("Arial", 30)

left_score = 0
right_score = 0

# set the game loop
run = True
while run:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # check for collisions with the top and bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= win_height:
        ball_speed_y *= -1
    
    # check for collisions with the left paddle
    if ball_x - ball_radius <= left_paddle_x + paddle_width and ball_y >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
        ball_speed_x *= -1
        left_score+=1
    
    # check for collisions with the right paddle
    if ball_x + ball_radius >= right_paddle_x and ball_y >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
        ball_speed_x *= -1
        right_score+=1
    
    # check for scoring on the left
    if ball_x - ball_radius <= 0:
        right_score += 1
        ball_x = int(win_width / 2)
        ball_y = int(win_height / 2)
        ball_speed_x = 5 * random.choice([-1, 1])
        ball_speed_y = 5 * random.choice([-1, 1])
    
    # check for scoring on the right
    if ball_x + ball_radius >= win_width:
        left_score += 1
        ball_x = int(win_width / 2)
        ball_y = int(win_height / 2)
        ball_speed_x = 5 * random.choice([-1, 1])
        ball_speed_y = 5 * random.choice([-1, 1])
    
    # move the left paddle to follow the ball
    if left_paddle_y + int(paddle_height / 2) < ball_y:
        left_paddle_y += paddle_speed
    elif left_paddle_y + int(paddle_height / 2) > ball_y:
        left_paddle_y -= paddle_speed
    
    # move the right paddle to follow the ball
    if right_paddle_y + int(paddle_height / 2) < ball_y:
        right_paddle_y+=paddle_speed

    elif right_paddle_y + int(paddle_height / 2) > ball_y:
        right_paddle_y -= paddle_speed

    # clear the window
    win.fill((0, 0, 0))

    # draw the ball
    pygame.draw.circle(win, ball_color, (ball_x, ball_y), ball_radius)

    # draw the left paddle
    pygame.draw.rect(win, paddle_color, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))

    # draw the right paddle
    pygame.draw.rect(win, paddle_color, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # draw the scores
    left_score_text = score_font.render(str(left_score), True, (255, 255, 255))
    right_score_text = score_font.render(str(right_score), True, (255, 255, 255))
    win.blit(left_score_text, (50, 50))
    win.blit(right_score_text, (win_width - 50 - right_score_text.get_width(), 50))

    # update the window
    pygame.display.update()

pygame.quit()
