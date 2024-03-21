import pygame
import time
from .o_wins_menu import display_o_menu
from .x_wins_menu import display_x_menu
from .tie_menu import display_tie_menu


def start_tiktaktoe(matrix, joystick_found, joystick, draw, image):
    
    global last_input_time
    global input_lock_time
    global y
    global x
    pygame.init()
    

    input_lock_time = 0.3
    last_input_time = 0
    initial_input_delay = 0.3
    dt = 0


    #Colors
    RED=(255, 0, 0)
    BLUE=(0, 0, 255)
    WHITE=(255, 255, 255)
    BLACK=(0, 0, 0)

    # defining the game field and general settings
    scale = 1
    pygame.display.set_caption('Tic Tac Tobi')

    # defining the moving rectangle
    x = 11*scale  # start position
    y = 1*scale
    vel = 10  # velocity


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
        global y
        global x
        

        current_time=time.time()
        # Schwellenwert für Stick-Drift oder Neutralzone
        if current_time - last_input_time > input_lock_time:
            x_axis = 0 if abs(x_axis) < threshold else x_axis
            y_axis = 0 if abs(y_axis) < threshold else y_axis
            # print(x_axis, y_axis)
            if x_axis < 0 and x < 21:
                x += vel
                last_input_time = current_time
            elif x_axis > 0 and x > 1:
                x -= vel
                last_input_time = current_time
            elif y_axis < 0 and y < 21:
                y += vel
                last_input_time = current_time
            elif y_axis > 0 and y > 1:
                y -= vel
                last_input_time = current_time

    while running:
        # print(player_circle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
        initial_input_delay = initial_input_delay-dt

        if joystick.get_button(8) and ((x,y) not in player_x) and len(player_circle) <= len(player_x) and game_over == False and player == 0 and (initial_input_delay <= 0):
            player_circle.add((x,y))
            player = 1
        if joystick.get_button(8) and ((x,y) not in player_circle) and (len(player_circle) > len(player_x)) and game_over == False and player == 1 and (initial_input_delay <= 0):
            player_x.add((x,y))
            player = 0

        #printing the game board
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


        #moving rectangle to trac position
        if player ==0:
            draw.rectangle((x ,y ,x+9,y+9),fill=BLUE)
        elif player == 1:
            draw.rectangle((x ,y ,x+9,y+9),fill=RED)
        draw.rectangle((x+1 ,y+1 ,x+8,y+8),fill=BLACK)

        #print(x)
        #print(y)

        #draws x or circle
        for b in player_circle:
            draw.ellipse((b[0] + 1, b[1] + 1, b[0] + 8,b[1] + 8),fill=BLUE)
            draw.ellipse((b[0] + 2, b[1] + 2, b[0] + 7,b[1] + 7),fill=BLACK)
        for i in player_x:
            draw.line((i[0] + 1, i[1] + 1, i[0] + 8,i[1] + 8),fill=RED)
            draw.line((i[0] + 1,i[1] + 8,i[0] + 8,i[1] + 1),fill=RED)

        #check for win for player_circle
        #Horizontal
        if (1*scale,1*scale) in player_circle and (11*scale,1*scale) in player_circle and (21*scale,1*scale) in player_circle : #wenn winner == true muss player_circle wins stehen und play again button
            print("h1")
            winner = 0
            game_over = True
        elif (1*scale,11*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,11*scale) in player_circle :
            print("h2")
            winner = 0
            game_over = True
        elif (1*scale,21*scale) in player_circle and (11*scale,21*scale) in player_circle and (21*scale,21*scale) in player_circle :
            print("h3")
            winner = 0
            game_over = True
        #Vertical
        elif (1*scale,1*scale) in player_circle and (1*scale,11*scale) in player_circle and (1*scale,21*scale) in player_circle :
            print("v1")
            winner = 0
            game_over = True
        elif (11*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (11*scale,21*scale) in player_circle :
            print("v2")
            winner = 0
            game_over = True
        elif (21*scale,1*scale) in player_circle and (21*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
            print("v3")
            winner = 0
            game_over = True
        #Diogonal
        elif (1*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
            print("d1")
            winner = 0
            game_over = True
        elif (1*scale,21*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,1*scale) in player_circle :
            print("d2")
            winner = 0
            game_over = True

        #check for win for player_x
        #Horizontal
        elif (1*scale,1*scale) in player_x and (11*scale,1*scale) in player_x and (21*scale,1*scale) in player_x :
            winner = 1
            game_over = True
        elif (1*scale,11*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,11*scale) in player_x :
            winner = 1
            game_over = True
        elif (1*scale,21*scale) in player_x and (11*scale,21*scale) in player_x and (21*scale,21*scale) in player_x :
            winner = 1
            game_over = True
        #Vertical
        elif (1*scale,1*scale) in player_x and (1*scale,11*scale) in player_x and (1*scale,21*scale) in player_x :
            winner = 1
            game_over = True
        elif (11*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (11*scale,21*scale) in player_x :
            winner = 1
            game_over = True
        elif (21*scale,1*scale) in player_x and (21*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
            winner = 1
            game_over = True
        #Diogonal
        elif (1*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
            winner = 1
            game_over = True
        elif (1*scale,21*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,1*scale) in player_x :
            winner = 1
            game_over = True

        #checks for tie
        elif len(player_circle) == 5 and len(player_x) == 4:
            print("tie1")
            winner = 2
            game_over = True
        elif len(player_circle) == 4 and len(player_x) == 5:
            print("tie2")
            winner = 2
            game_over = True

        #End_test who has won
        if game_over == True and winner == 0:
            # o win
            running = display_o_menu(matrix, joystick_found, joystick, draw, image)
            player_circle = set([])
            player_x = set([])
            print("player_x",player_x)
            game_over = False
            player = 0
            winner = -1
            time.sleep(0.3)
            initial_input_delay=0.3

        elif game_over == True and winner == 1:
            # x win
            running = display_x_menu(matrix, joystick_found, joystick, draw, image)
            player_circle = set([])
            player_x = set([])
            game_over = False
            player = 0
            winner = -1
            time.sleep(0.3)
            initial_input_delay=0.3
        elif game_over == True and winner == 2:
            # tie
            running = display_tie_menu(matrix, joystick_found, joystick, draw, image)
            player_circle = set([])
            player_x = set([])
            game_over = False
            player = 0
            winner = -1
            time.sleep(0.3)
            initial_input_delay=0.3
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
                running = False  # ends pygamges
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60)/1000