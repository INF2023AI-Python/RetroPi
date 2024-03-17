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

joystick_found = True
pygame.init()
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
PLAY_COLOR = WHITE
EXIT_COLOR = WHITE
BORDER_COLOR = WHITE

RETURN = 0

running = True
x = 0
play_color = (GREEN)
exit_color = (WHITE)

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_menu():
    #draw M
    draw.rectangle((5,3,5,7), fill=(WHITE))
    draw.rectangle((6,4,6,4), fill=(WHITE))
    draw.rectangle((7,5,7,5), fill=(WHITE))
    draw.rectangle((8,4,8,4), fill=(WHITE))
    draw.rectangle((9,3,9,7), fill=(WHITE))

    #draw e
    draw.rectangle((11,3,15,3), fill=(WHITE))
    draw.rectangle((11,3,11,7), fill=(WHITE))
    draw.rectangle((11,5,14,5), fill=(WHITE))
    draw.rectangle((11,7,15,7), fill=(WHITE))
    #draw n
    draw.rectangle((17,3,17,7), fill=(WHITE))
    draw.rectangle((18,4,18,4), fill=(WHITE))
    draw.rectangle((19,5,19,5), fill=(WHITE))
    draw.rectangle((20,6,20,6), fill=(WHITE))
    draw.rectangle((21,3,21,7), fill=(WHITE))
    #draw u
    draw.rectangle((23,3,23,7), fill=(WHITE))
    draw.rectangle((24,7,26,7), fill=(WHITE))
    draw.rectangle((26,3,26,7), fill=(WHITE))

    #draws underline for Menu
    draw.rectangle((3,9,28,9),fill=(WHITE))
    draw.rectangle((3,7,3,9),fill=(WHITE))
    draw.rectangle((28,7,28,9),fill=(WHITE))

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

def move_box():
    global play_color
    global exit_color
    global running
    global x
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

def move_box_joy(x_axis):
    threshold = 0.1
    global play_color
    global exit_color
    global running
    global x
    print("joy")
    x_axis = 0 if abs(x_axis) < threshold else x_axis
    if x_axis > 0 and x == 13:
        x = 0
        print("x = 0")
    elif x_axis < 0 and x == 0:
        x = 13
        print("x = 13")

    if joystick.get_button(RETURN):
        if x == 0:
            print("PLAY")
            running = False
        if x == 13:
            print("EXIT")
            running = False

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
while running:

    if joystick_found:
        x_axis = joystick.get_axis(0)
        move_box_joy(x_axis)
    else:
        move_box()
    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw_menu()
    draw_box(x)
    draw_arrow(play_color)
    draw_exit(exit_color)

    matrix.SetImage(image, 0, 0)
    clock.tick(15)
