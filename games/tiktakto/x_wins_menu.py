import pygame
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

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

RETURN = 8

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_x(color):
    #draws x
    draw.line((3,3,7,7), fill=(color))
    draw.line((7,3,3,7), fill=(color))

def draw_winmenu(text_color):
    #draw w
    draw.rectangle((11,3,11,7), fill=(text_color))
    draw.point ((12,6), fill=(text_color))
    draw.point ((13,5), fill=(text_color))
    draw.point ((14,6), fill=(text_color))
    draw.rectangle((15,3,15,7), fill=(text_color))

    #draw i
    draw.rectangle((17,3,17,7), fill=(text_color))

    #draw n
    draw.rectangle((19,3,19,7), fill=(text_color))
    draw.rectangle((20,4,20,4), fill=(text_color))
    draw.rectangle((21,5,21,5), fill=(text_color))
    draw.rectangle((22,6,22,6), fill=(text_color))
    draw.rectangle((23,3,23,7), fill=(text_color))

    #draw s
    draw.rectangle((25,3,28,3), fill=(WHITE))
    draw.point((25,4), fill=(WHITE))
    draw.rectangle((25,5,28,5), fill=(WHITE))
    draw.point((28,6), fill=(WHITE))
    draw.rectangle((25,7,28,7), fill=(WHITE))

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
        play_color = (GREEN)
        exit_color = (WHITE)
    elif x_axis < 0 and x == 0:
        x = 13
        play_color = (WHITE)
        exit_color = (RED)
        print("x = 13")

    if joystick.get_button(RETURN):
        if x == 0:
            print("PLAY")
            running = False
        if x == 13:
            print("EXIT")
            running = False


clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
pygame.init()
running = True
x = 0
play_color = (GREEN)
exit_color = (WHITE)
while running:
    if joystick_found:
        x_axis = joystick.get_axis(0)
        move_box_joy(x_axis)
    else:
        move_box()

    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw_x(WHITE)
    draw_winmenu(WHITE)
    draw_box(x)
    draw_arrow(play_color)
    draw_exit(exit_color)

    matrix.SetImage(image, 0, 0)
    clock.tick(60)