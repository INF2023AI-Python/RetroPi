import pygame
import os
from game_object import *
from PIL import Image
from PIL import ImageDraw

try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

pygame.init()
SCALE = 1

##screen = pygame.display.set_mode((32*SCALE, 32*SCALE),pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 1 # TODO REMOVE VAR
score = 0

PLAYER_SPEED = 1
BALL_SPEED = 1

player = GameObject(pygame.Rect(0, 16, 1 * SCALE, 6 * SCALE), pygame.Vector2(0, PLAYER_SPEED))
ball = GameObject(pygame.Rect((16), (16), 1 * SCALE, 1 * SCALE), pygame.Vector2(BALL_SPEED, -BALL_SPEED))

# ball_pos = pygame.Vector2((screen.get_width()/2), (screen.get_height()/2))
playing_field = pygame.Rect(0, 0, 32 * SCALE, 32 * SCALE)


# next_tick_ball = pygame.Vector2(0,0)

def withinBoard(rect: pygame.Rect):
    return playing_field.contains(rect)


image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    ##screen.fill("black")

    wall = pygame.Rect(32 * SCALE, 0, 1 * SCALE, 32 * SCALE)

    # ball_box = pygame.Rect(ball_pos.x,ball_pos.y,10,10)

    # draw gameobjects
    ##pygame.draw.rect(screen, "white", wall)
    ##pygame.draw.rect(screen, "black", playing_field)
    ##pygame.draw.rect(screen, "white", player.rect)
    ##pygame.draw.rect(screen, "white", ball.rect)

    draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0, 0))
    draw.rectangle((31, 0, 31, 31), fill=(255, 255, 255, 0))
    draw.rectangle((player.rect.left, player.rect.top, playing_field.left, player.rect.bottom), fill=(255, 255, 255))
    draw.rectangle((ball.rect.left, ball.rect.top, ball.rect.left, ball.rect.top), fill=(255, 255, 255))
    matrix.SetImage(image, 0, 0)
    # update variable for gameobjects
    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and withinBoard(player.rect):
        if (player.rect.top - (player.speed.y * dt)) < 0:
            player.rect.top = 0
        else:
            player.rect.top -= player.speed.y * dt

    if keys[pygame.K_s] and withinBoard(player.rect):
        if (player.rect.bottom + (player.speed.y * dt)) > (32 * SCALE):
            player.rect.top = 32 * SCALE - player.rect.height
        else:
            player.rect.top += player.speed.y * dt

    # BALL MOVEMENT

    # collide left and right
    if ball.rect.top < playing_field.top or ball.rect.bottom >= playing_field.bottom:
        ball.speed.y *= -1
        if ball.rect.top < playing_field.top - 1 * SCALE:
            ball.rect.top = playing_field.top
        if ball.rect.bottom >= playing_field.bottom:
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
        # end_screen_img = pygame.image.load('/endscreen.png')
        # screen.blit(end_screen_img,playing_field)
        # ball.speed.x *= -1
        # ball.rect.left = playing_field.left
        print(ball.rect, playing_field)
        print("your score score", score)
        break
    # collide player

    # update position
    ball.rect.top = ball.rect.top + ball.speed.y * dt
    ball.rect.left = ball.rect.left + ball.speed.x * dt

    # flip() the display to put your work on screen
    ##pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(30)

pygame.quit()
