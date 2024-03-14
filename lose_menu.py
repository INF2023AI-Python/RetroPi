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
LIGHT_BLUE = (0,255,255)
PLAY_COLOR = WHITE
EXIT_COLOR = WHITE
BORDER_COLOR = WHITE

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_losemenu():
    #draw L
    draw.rectangle((5,3,5,7), fill=(WHITE))
    draw.rectangle((6,7,8,7), fill=(WHITE))

    #draw O
    draw.rectangle((10,3,14,7), fill=(WHITE))
    draw.rectangle((11,4,13,6), fill=(BLACK))

    #draw S
    draw.rectangle((16,3,20,3), fill=(WHITE))
    draw.point((16,4), fill=(WHITE))
    draw.rectangle((16,5,20,5), fill=(WHITE))
    draw.point((20,6), fill=(WHITE))
    draw.rectangle((16,7,20,7), fill=(WHITE))

    #draw E
    draw.rectangle((22,3,22,7), fill=(WHITE))
    draw.rectangle((23,3,26,3), fill=(WHITE))
    draw.rectangle((23,5,25,5), fill=(WHITE))
    draw.rectangle((23,7,26,7), fill=(WHITE))

    #draws underline for Menu
    draw.rectangle((3,9,28,9),fill=(WHITE))
    draw.rectangle((3,7,3,9),fill=(WHITE))
    draw.rectangle((28,7,28,9),fill=(WHITE))

def draw_box(x):
    #draws box for play arrow
    draw.rectangle((2+x,11,2+x,21),fill=(BORDER_COLOR))
    draw.rectangle((2+x,11,10+x,11),fill=(BORDER_COLOR))
    draw.rectangle((10+x,11,10+x,21),fill=(BORDER_COLOR))
    draw.rectangle((2+x,21,10+x,21),fill=(BORDER_COLOR))

def draw_arrow(color):
    #draws arrow
    draw.rectangle((5,14,5,18),fill=(color))
    draw.rectangle((6,15,6,17),fill=(color))
    draw.rectangle((7,16,7,16),fill=(color))

def draw_exit(color):
    #draws x
    draw.point((24,15),fill=(color))
    draw.point((25,16),fill=(color))
    draw.point((26,17),fill=(color))
    draw.point((27,18),fill=(color))
    draw.point((28,19),fill=(color))
    draw.point((24,19),fill=(color))
    draw.point((25,18),fill=(color))
    draw.point((26,17),fill=(color))
    draw.point((27,16),fill=(color))
    draw.point((28,15),fill=(color))

def draw_save(color):
    #draws save
    draw.rectangle((15,13,15,19),fill=(color))
    draw.rectangle((16,13,16,20),fill=(color))
    draw.rectangle((17,13,17,19),fill=(color))
    draw.rectangle((13,17,19,17),fill=(color))
    draw.rectangle((14,18,18,18),fill=(color))

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
pygame.init()
running = True
x = 0
play_color = (GREEN)
exit_color = (WHITE)
save_color = (WHITE)
while running:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:  #movment of the select box
        x -= 10
    if keys[pygame.K_RIGHT] and x <= 10:
        x += 10

    #sets the colors for the content of the boxes
    if x == 0:
        play_color = (GREEN)
        save_color = (WHITE)
        exit_color = (WHITE)
    if x == 10:
        play_color = (WHITE)
        save_color = (LIGHT_BLUE)
        exit_color = (WHITE)
    if x == 20:
        play_color = (WHITE)
        save_color = (WHITE)
        exit_color = (RED)

    if keys[pygame.K_RETURN]: #if enter is pressed
        if x == 0:
            print("PLAY")
            running = False
        if x == 10:
            print("SAVE")
            running = False
        if x == 20:
            print("EXIT")
            running = False

    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw_losemenu()
    draw_box(x)
    draw_arrow(play_color)
    draw_exit(exit_color)
    draw_save(save_color)

    matrix.SetImage(image, 0, 0)
    clock.tick(10)
