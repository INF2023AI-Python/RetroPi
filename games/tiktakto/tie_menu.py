import pygame
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

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
PLAY_COLOR = WHITE
EXIT_COLOR = WHITE
BORDER_COLOR = WHITE

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_tiemenu(text_color):
    #draws T
    draw.line((7,1,13,1),fill=(WHITE))
    draw.line((10,1,10,7),fill=(WHITE))

    #draws I
    draw.line((16,1,16,7),fill=(WHITE))

    #draws E
    draw.line((19,1,19,7),fill=(WHITE))
    draw.line((19,1,24,1),fill=(WHITE))
    draw.line((19,4,23,4),fill=(WHITE))
    draw.line((19,7,24,7),fill=(WHITE))

    #draws underline for Menu
    draw.rectangle((1,9,30,9),fill=(WHITE))
    draw.rectangle((1,7,1,9),fill=(WHITE))
    draw.rectangle((30,7,30,9),fill=(WHITE))


def draw_box(x):
    #draws box for play arrow
    draw.rectangle((5+x,11,5+x,21),fill=(BORDER_COLOR))
    draw.rectangle((5+x,11,13+x,11),fill=(BORDER_COLOR))
    draw.rectangle((13+x,11,13+x,21),fill=(BORDER_COLOR))
    draw.rectangle((5+x,21,13+x,21),fill=(BORDER_COLOR))

def draw_arrow(color):
    #draws arrow
    draw.rectangle((8,14,8,18),fill=(color))
    draw.rectangle((9,15,9,17),fill=(color))
    draw.rectangle((10,16,10,16),fill=(color))

def draw_exit(color):
    #draws x
    draw.point((20,14),fill=(color))
    draw.point((21,15),fill=(color))
    draw.point((22,16),fill=(color))
    draw.point((23,17),fill=(color))
    draw.point((24,18),fill=(color))
    draw.point((20,18),fill=(color))
    draw.point((21,17),fill=(color))
    draw.point((22,16),fill=(color))
    draw.point((23,15),fill=(color))
    draw.point((24,14),fill=(color))

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
pygame.init()
running = True
x = 0
play_color = (GREEN)
exit_color = (WHITE)
while running:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x < 14:  #movment of the select box
        if x > 0:
            x = 0
            play_color = (GREEN)
            exit_color = (WHITE)
    if keys[pygame.K_RIGHT] and x < 12:
        if x < 13:
            x = 13
            exit_color = (RED)
            play_color = (WHITE)

    if keys[pygame.K_RETURN]: #if enter is pressed
        if x == 0:
            print("PLAY")
            running = False
        if x == 13:
            print("EXIT")
            running = False
    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw_tiemenu(WHITE)
    draw_box(x)
    draw_arrow(play_color)
    draw_exit(exit_color)

    matrix.SetImage(image, 0, 0)
    clock.tick(15)