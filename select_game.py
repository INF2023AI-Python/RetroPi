import pygame
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

PURPLE = (79,0,153)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
DARK_BLUE = (0,8,175)
RED = (255,0,0)
YELLOW = (255,221,0)
LIGHT_YELLOW = (255,238,132)
GREEN = (0,255,0)
LIGHT_GREEN = (70,230,0)
GREY = (128,128,128)
DARK_GREY = (64,64,64)
LIGHT_GREY = (192,192,192)

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_grid():
    #draws big rectangle over the whole grid and cuts out the middle painted black
    draw.rectangle((0,0,32,32),fill=(PURPLE))
    draw.rectangle((1,1,30,30),fill=(BLACK))

    #draws the gridlines
    draw.line((10,0,10,32),fill=(PURPLE))
    draw.line((21,0,21,32),fill=(PURPLE))
    draw.line((0,10,32,10),fill=(PURPLE))
    draw.line((0,21,32,21),fill=(PURPLE))

    #draws the small squares in the corners in the middlefield
    draw.point((11,11),fill=(PURPLE))
    draw.point((11,20),fill=(PURPLE))
    draw.point((20,11),fill=(PURPLE))
    draw.point((20,20),fill=(PURPLE))

def draw_space_invader(color_mob, color_rock, color_base, color_player, color_bullet):
    #draws the mob
    for i in range (2):
        for ii in range (4):
            draw.point((2+(2*ii),12+(2*i)),fill=(color_mob))
    draw.point((4,14),fill=(BLACK))
    #draws the rock
    draw.rectangle((1,16,2,17),fill=(color_rock))
    draw.point((1,16),fill=(BLACK))
    draw.rectangle((7,17,8,18),fill=(color_rock))
    draw.point((7,18),fill=(BLACK))
    #draws the player
    draw.point((4,19),fill=(color_player))
    #draws the bullets
    draw.point((4,13),fill=(color_bullet))
    draw.point((4,16),fill=(color_bullet))
    #draws the base
    draw.line((1,20,9,20),fill=(color_base))

def draw_snake(color_head, color_body, color_apple):
    #draws the snake body
    draw.line((12,3,12,5),fill=(color_body))
    draw.line((13,5,13,7),fill=(color_body))
    draw.point((14,7),fill=(color_body))
    #draws the snake head
    draw.point((15,7),fill=(color_head))
    #draws the apple
    draw.point((18,2),fill=(color_apple))

def draw_tiktaktoe(color_red, color_blue, color_white):
    #draws the grid
    draw.line((24,1,24,9),fill=(color_white))
    draw.line((28,1,28,9),fill=(color_white))
    draw.line((22,3,30,3),fill=(color_white))
    draw.line((22,7,30,7),fill=(color_white))
    #draws blue
    draw.rectangle((25,1,27,2),fill=(color_blue))
    draw.rectangle((22,4,23,6),fill=(color_blue))
    draw.rectangle((29,8,30,9),fill=(color_blue))
    #draws red
    draw.rectangle((29,1,30,2),fill=(color_red))
    draw.rectangle((25,4,27,6),fill=(color_red))

def draw_pong(color_player_wall, color_ball):
    #draws the player
    draw.line((1,2,1,5),fill=(color_player_wall))
    #draws the wall
    draw.line((9,1,9,9),fill=(color_player_wall))
    #draws the ball
    draw.point((3,3),fill=(color_ball))

def draw_python_logo():
    #draws the Blue part of the Snake (top to bottom)
    draw.rectangle((13,10,17,12),fill=(BLUE))
    draw.rectangle((16,11,18,14),fill=(BLUE))
    draw.rectangle((12,14,17,15),fill=(BLUE))
    draw.rectangle((11,15,12,17),fill=(BLUE))
    draw.point((12,18),fill=(BLUE))
    draw.point((13,16),fill=(BLUE))
    #draws the Yellow part of the Snake (top to bottom)
    draw.point((19,13),fill=(YELLOW))
    draw.rectangle((19,14,20,16),fill=(YELLOW))
    draw.point((18,15),fill=(YELLOW))
    draw.rectangle((14,16,19,17),fill=(YELLOW))
    draw.rectangle((13,17,15,20),fill=(YELLOW))
    draw.rectangle((14,19,18,21),fill=(YELLOW))
    #draws the eyes
    draw.point((14,11),fill=(BLACK))
    draw.point((17,20),fill=(BLACK))

def draw_endless_runner(color_wall, color_player, color_obstacle):
    #draws the wall
    draw.line((22,11,30,11),fill=(color_wall))
    draw.line((22,20,30,20),fill=(color_wall))
    #draws the player
    draw.point((23,19),fill=(color_player))
    #draws the obstacle
    draw.point((25,19),fill=(color_obstacle))
    draw.point((27,12),fill=(color_obstacle))
    draw.point((28,14),fill=(color_obstacle))
    draw.point((29,19),fill=(color_obstacle))

def draw_button_test(color_button, color_3D_effect):
    #draws the button
    draw.rectangle((4,23,6,28),fill=(color_button))
    draw.rectangle((2,25,8,26),fill=(color_button))
    draw.point((3,24),fill=(color_button))
    draw.point((3,27),fill=(color_button))
    draw.point((7,24),fill=(color_button))
    draw.point((7,27),fill=(color_button))
    #draws the 3D effect of the button
    draw.line((2,27,2,28),fill=(color_3D_effect))
    draw.line((3,28,3,29),fill=(color_3D_effect))
    draw.rectangle((4,29,6,30),fill=(color_3D_effect))
    draw.line((7,28,7,29),fill=(color_3D_effect))
    draw.line((8,27,8,28),fill=(color_3D_effect))

def draw_trophy(color_body,color_shiny,color_darker):
    #draws the trophy
    draw.rectangle((13,23,18,25),fill=(color_body))
    draw.line((14,26,17,26),fill=(color_body))
    draw.rectangle((15,27,16,28),fill=(color_body))
    draw.line((14,29,17,29),fill=(color_body))
    #draws the shiny part of the trophy
    draw.line((17,23,17,24),fill=(color_shiny))
    draw.point((16,25),fill=(color_shiny))

def draw_shutdown_button(color):
    #draws the button from left to the right
    draw.point((24,24),fill=(color))
    draw.line((23,25,23,27),fill=(color))
    draw.point((24,28),fill=(color))
    draw.line((25,29,27,29),fill=(color))
    draw.point((28,28),fill=(color))
    draw.line((29,27,29,25),fill=(color))
    draw.point((28,24),fill=(color))
    draw.line((26,23,26,25),fill=(color))

running = True
while running:
    draw_grid()
    draw_space_invader(RED, GREY ,GREEN, BLUE, WHITE)
    draw_snake(YELLOW, BLUE, RED)
    draw_tiktaktoe(RED, BLUE, WHITE)
    draw_pong(WHITE, RED)
    draw_python_logo()
    draw_endless_runner(WHITE, BLUE, RED)
    draw_button_test(BLUE, DARK_BLUE)
    draw_trophy(YELLOW, WHITE, LIGHT_YELLOW)
    draw_shutdown_button(RED)
    matrix.SetImage(image, 0, 0)