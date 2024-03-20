import pygame
import time
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

pygame.init()

#delay
input_lock_time = 0.3
last_input_time = 0

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
RED=(255, 0, 0)
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

# defining the game field and general settings
scale = 1
pygame.display.set_caption('Tic Tac Tobi')
color = (255, 0, 0)

# defining the moving rectangle
x = 11*scale  # start position
y = 1*scale
vel = 10*scale  # velocity

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
running = True
game_over = False
player= 0

#Tuple to write positions x and y
player_circle = set([])
player_x = set([])

def move_box_joy(x_axis, y_axis, threshold=0.1):
        global last_input_time
        global input_lock_time
        global snake_dir
        global y
        global x

        current_time=time.time()
        # Schwellenwert für Stick-Drift oder Neutralzone
        if current_time - last_input_time > input_lock_time:
            x_axis = 0 if abs(x_axis) < threshold else x_axis
            y_axis = 0 if abs(y_axis) < threshold else y_axis
            #print(x_axis, y_axis)
            if x_axis < 0 and x < 21*scale:
                x += vel
                last_input_time = current_time
            elif x_axis > 0 and x > 1*scale:
                x -= vel
                last_input_time = current_time
            elif y_axis < 0 and y < 21*scale:
                y += vel
                last_input_time = current_time
            elif y_axis > 0 and y > 1*scale:
                y -= vel
                last_input_time = current_time

def draw_grid():
    draw.rectangle((0,0,32,32),fill=WHITE)

    draw.rectangle((2,2,9,9),fill=BLACK)
    draw.rectangle((12,2,19,9),fill=BLACK)
    draw.rectangle((22,2,29,9),fill=BLACK)

    draw.rectangle((2,12,9,19),fill=BLACK)
    draw.rectangle((12,12,19,19),fill=BLACK)
    draw.rectangle((22,12,29,19),fill=BLACK)

    draw.rectangle((2,22,9,29),fill=BLACK)
    draw.rectangle((12,22,19,29),fill=BLACK)
    draw.rectangle((22,22,29,29),fill=BLACK)

def check_win_player_circle():
    #Horizontal
    if (1*scale,1*scale) in player_circle and (11*scale,1*scale) in player_circle and (21*scale,1*scale) in player_circle : #wenn winner == true muss player_circle wins stehen und play again button
        winner = 0
        game_over = True
    if (1*scale,11*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,11*scale) in player_circle :
        winner = 0
        game_over = True
    if (1*scale,21*scale) in player_circle and (11*scale,21*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    #Vertical
    if (1*scale,1*scale) in player_circle and (1*scale,11*scale) in player_circle and (1*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (11*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (11*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (21*scale,1*scale) in player_circle and (21*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    #Diogonal
    if (1*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (1*scale,21*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,1*scale) in player_circle :
        winner = 0
        game_over = True

def check_win_player_x():
    #Horizontal
    if (1*scale,1*scale) in player_x and (11*scale,1*scale) in player_x and (21*scale,1*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,11*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,11*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,21*scale) in player_x and (11*scale,21*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    #Vertical
    if (1*scale,1*scale) in player_x and (1*scale,11*scale) in player_x and (1*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (11*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (11*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (21*scale,1*scale) in player_x and (21*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    #Diogonal
    if (1*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,21*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,1*scale) in player_x :
        winner = 1
        game_over = True

def check_tie(): 
    if len(player_circle) == 5 and len(player_x) == 4:
        winner = 2
        game_over = True
    if len(player_circle) == 4 and len(player_x) == 5:
        winner = 2
        game_over = True

while running:
    #Can close the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # imput from the joystick 
    if joystick_found:
        if joystick.get_button(10):
            running = False
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)
        move_box_joy(x_axis, y_axis)
    else:
        #movment of the blue box
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 1*scale:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 21*scale:
            x += vel
        if keys[pygame.K_UP] and y > 1*scale:
            y -= vel
        if keys[pygame.K_DOWN] and y < 21*scale:
            y += vel

    #condition to draw a cirlce or an x
    if joystick.get_button(8) and ((x,y) not in player_x) and len(player_circle) <= len(player_x) and game_over == False and player == 0:
        player_circle.add((x,y))
        player = 1
    if joystick.get_button(8) and ((x,y) not in player_circle) and (len(player_circle) > len(player_x)) and game_over == False and player == 1:
        player_x.add((x,y))
        player = 0

    #printing the game board
    draw_grid()

    #moving rectangle to trac position
    if player ==0:
        draw.rectangle((x ,y ,x+9,y+9),fill=BLUE)
    elif player == 1:
        draw.rectangle((x ,y ,x+9,y+9),fill=RED)
    draw.rectangle((x+1 ,y+1 ,x+8,y+8),fill=BLACK)

    #draws x or circle
    for b in player_circle:
        draw.ellipse((b[0] + 1, b[1] + 1, b[0] + 8,b[1] + 8),fill=BLUE)
        draw.ellipse((b[0] + 2, b[1] + 2, b[0] + 7,b[1] + 7),fill=BLACK)
    for i in player_x:
        draw.line((i[0] + 1, i[1] + 1, i[0] + 8,i[1] + 8),fill=RED)
        draw.line((i[0] + 1,i[1] + 8,i[0] + 8,i[1] + 1),fill=RED)

    #check for win for player_circle
    check_win_player_circle()

    #check for win for player_x
    check_win_player_x()
    
    #checks for tie
    check_tie()

    #End_test who has won
    if game_over == True and winner == 0:
        #ruft o wins auf
        pass
    if game_over == True and winner == 1:
         #ruft x wins auf
        pass
    if game_over == True and winner == 2:
         #ruft tie auf. tie fehlt auf matrix ?
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
            running = False  # ends pygamges
    matrix.SetImage(image, 0, 0)
    clock.tick(30) 



