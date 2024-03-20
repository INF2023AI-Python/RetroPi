import pygame
import time
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

pygame.init()

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

joystick_found = True
#Joystick
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    #print("Kein Joystick gefunden")

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

#Colors
YELLOW=(0, 255, 0)
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

#delay
input_lock_time = 0.3
last_input_time = 0

pygame.display.set_caption('Tic Tac Tobi')

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
running = True


def move_box_joy(x_axis, y_axis, threshold=0.1):
        global last_input_time
        global input_lock_time

        current_time=time.time()
        # Schwellenwert für Stick-Drift oder Neutralzone
        if current_time - last_input_time > input_lock_time:
            x_axis = 0 if abs(x_axis) < threshold else x_axis
            y_axis = 0 if abs(y_axis) < threshold else y_axis
            #print(x_axis, y_axis)
            if x_axis:
                #x -+= vel
                draw.line((5,2,0,2),fill=WHITE)
                draw.line((5,2,3,0),fill=WHITE)
                draw.line((5,2,3,4),fill=WHITE)
                last_input_time = current_time
            elif x_axis:
                #x -= vel
                draw.line((0,2,6,2),fill=WHITE)
                draw.line((0,2,2,0),fill=WHITE)
                draw.line((0,2,2,4),fill=WHITE)
                last_input_time = current_time
            elif y_axis:
                #y += vel
                draw.line((0,2,2,0),fill=WHITE)
                draw.line((2,0,4,2),fill=WHITE)
                draw.line((2,1,2,5),fill=WHITE)
                last_input_time = current_time
            elif y_axis :
                #y -= vel
                draw.line((2,0,2,4),fill=WHITE)
                draw.line((0,3,2,5),fill=WHITE)
                draw.line((2,5,4,3),fill=WHITE)
                last_input_time = current_time



if joystick.get_button(8):
    draw.ellipse((0, 0, 10,10),fill=YELLOW)
if joystick.get_button(9):
    draw.ellipse((0, 0, 10,10),fill=BLUE)
if joystick.get_button(10):
    draw.ellipse((0, 0, 10,10),fill=YELLOW)
if joystick.get_button(11):
    draw.ellipse((0, 0, 10,10),fill=BLUE)

while running:
    #Can close the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # imput from the joystick 
    if joystick_found:
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)
        move_box_joy(x_axis, y_axis)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
            running = False  # ends pygamges
    matrix.SetImage(image, 0, 0)
    clock.tick(30) 
