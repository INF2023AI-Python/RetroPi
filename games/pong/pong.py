import pygame
import os
from game_object import *

pygame.init()
SCALE = 30

screen = pygame.display.set_mode((32*SCALE, 32*SCALE),pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
score = 0

PLAYER_SPEED = 20*SCALE
BALL_SPEED = 20*SCALE

player = GameObject(pygame.Rect(0,screen.get_height()/2,1*SCALE,6*SCALE),pygame.Vector2(0,PLAYER_SPEED))
ball = GameObject(pygame.Rect((screen.get_width()/2), (screen.get_height()/2),1*SCALE,1*SCALE),pygame.Vector2(BALL_SPEED,-BALL_SPEED))


# ball_pos = pygame.Vector2((screen.get_width()/2), (screen.get_height()/2))
playing_field = pygame.Rect(0,0,32*SCALE,32*SCALE)

# next_tick_ball = pygame.Vector2(0,0)

def withinBoard(rect:pygame.Rect):
    return playing_field.contains(rect)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    wall = pygame.Rect(32*SCALE, 0, 1*SCALE, 32*SCALE)
    # ball_box = pygame.Rect(ball_pos.x,ball_pos.y,10,10)

    # draw gameobjects
    pygame.draw.rect(screen, "white", wall)
    pygame.draw.rect(screen, "black", playing_field)
    pygame.draw.rect(screen, "white", player.rect)
    pygame.draw.rect(screen, "white", ball.rect)

    # update variable for gameobjects
    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and withinBoard(player.rect):
        if (player.rect.top - (player.speed.y * dt)) < 0:
            player.rect.top = 0
        else:
            player.rect.top -= player.speed.y * dt

    if keys[pygame.K_s] and withinBoard(player.rect):
        if (player.rect.bottom + (player.speed.y * dt)) > (32*SCALE):
            player.rect.top=32*SCALE-player.rect.height
        else:
            player.rect.top += player.speed.y* dt



    # BALL MOVEMENT

    # collide left and right
    if ball.rect.top < playing_field.top or ball.rect.bottom >= playing_field.bottom:
        ball.speed.y *= -1
        if ball.rect.top < playing_field.top-1*SCALE:
            ball.rect.top = playing_field.top
        if ball.rect.bottom  >= playing_field.bottom:
            ball.rect.bottom = playing_field.bottom

    
    # collide right
    if ball.rect.colliderect(wall):
        ball.speed.x *= -1
        ball.rect.right = wall.left
    # collide left
    elif ball.rect.colliderect(player.rect):
        ball.speed.x *= -1
        ball.rect.left = player.rect.right
        score += 1
    elif ball.rect.left <= playing_field.left:
        #end_screen_img = pygame.image.load('/endscreen.png')
        #screen.blit(end_screen_img,playing_field)
        # ball.speed.x *= -1
        # ball.rect.left = playing_field.left
        print("your score score", score)
        break
    # collide player
        
    # update position
    ball.rect.top = ball.rect.top + ball.speed.y* dt
    ball.rect.left = ball.rect.left + ball.speed.x* dt
    



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    

pygame.quit()