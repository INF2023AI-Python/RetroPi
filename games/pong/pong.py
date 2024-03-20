import pygame
import os
from game_object import *
from PIL import Image
from PIL import ImageDraw

try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions


pygame.init()
joystick_found = True
SCALE = 1
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and within_board(player.rect):
        next_y = player.rect.top - (player.speed.y * dt)
        player.rect.top = max(0,min(31-6,next_y))

    if keys[pygame.K_s] and within_board(player.rect):
        next_y = player.rect.top + (player.speed.y * dt)
        player.rect.top = max(0,min(31-6,next_y))

def move_joy(y_axis, threshold=0.1):
    y_axis = 0 if abs(y_axis) < threshold else y_axis
    if y_axis > 0:
        next_y = player.rect.top - (player.speed.y * dt)
        player.rect.top = max(0,min(31-6,next_y))
    elif y_axis < 0:
        next_y = player.rect.top + (player.speed.y * dt)
        player.rect.top = max(0,min(31-6,next_y))

def draw_walls(draw):
    draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0, 0))
    draw.rectangle((31, 0, 31, 31), fill=(255, 255, 255, 0))

def within_board(rect: pygame.Rect):
    return playing_field.contains(rect)


clock = pygame.time.Clock()
image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)
running = True
dt = 1  # TODO REMOVE VAR
score = 0

PLAYER_SPEED = 1
BALL_SPEED = 1

player = GameObject(pygame.Rect(0, 16, 1 , 6 ), pygame.Vector2(0, PLAYER_SPEED))
ball = GameObject(pygame.Rect((16), (16), 1 , 1 ), pygame.Vector2(BALL_SPEED, -BALL_SPEED))
playing_field = pygame.Rect(0, 0, 31 , 31 )
wall = pygame.Rect(31 , 0, 1 , 31 )

# game loop
while running:

    # player movement
    if joystick_found:
        y_axis = joystick.get_axis(1)
        move_joy(y_axis)
    else:
        move()
        # Check for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Ball Movement
    # Collision top / bottom
    if ball.rect.top < playing_field.top or ball.rect.bottom >= playing_field.bottom:
        ball.speed.y *= -1
        if ball.rect.top < playing_field.top - 1:
            ball.rect.top = playing_field.top
        if ball.rect.bottom >= playing_field.bottom:
            ball.rect.bottom = playing_field.bottom

    # Collision right
    if ball.rect.colliderect(wall):
        ball.speed.x *= -1
        ball.rect.right = wall.left
    # Collision Left / player
    elif ball.rect.colliderect(player.rect):
        ball.speed.x *= -1
        ball.rect.left = player.rect.right
        score += 1
    # lose condition
    elif ball.rect.right < playing_field.left:
        print("your score score", score)
        running = False

    # update position
    ball.rect.top = ball.rect.top + ball.speed.y * dt
    ball.rect.left = ball.rect.left + ball.speed.x * dt

    # draw image
    draw_walls(draw)
    draw.rectangle((player.rect.left, player.rect.top, playing_field.left, player.rect.bottom), fill=(255, 255, 255))
    draw.rectangle((ball.rect.left, ball.rect.top, ball.rect.left, ball.rect.top), fill=(255, 255, 255))
    # update matrix
    matrix.SetImage(image, 0, 0)
    
    # limits FPS to 30
    clock.tick(30)

pygame.quit()