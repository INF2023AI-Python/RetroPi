import pygame
import time
# from .o_wins_menu import display_o_menu
# from .x_wins_menu import display_x_menu
# from .tie_menu import display_tie_menu


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


    menu_delay = 0.3
    menu_move_value = -1
    #Colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    PLAY_COLOR = WHITE
    EXIT_COLOR = WHITE
    BORDER_COLOR = WHITE

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

    # winner:-2: reset_vars| -1=spielbar|0=o-win|1=
    winner = -1

    def menu_movement(joystick,value):
        x_axis = joystick.get_axis(0)
        if x_axis > 0.1:
            value = -1
        elif x_axis < -0.1:
            value = 1
        return value

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

    def draw_x(color):
        #draws x
        draw.line((3,3,7,7), fill=(color))
        draw.line((7,3,3,7), fill=(color))

    def draw_o(color):
        #draws o
        draw.ellipse((3,3,7,7), fill=(color))
        draw.rectangle((4,4,6,6), fill=(BLACK))

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
            # #print(x_axis, y_axis)
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

    # xplay
    # xquit
    # oplay
    # oquit
    # tieplay
    # tiequit
    
    def menu_x_play():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_winmenu((255,255,255))
        draw_x((255,255,255))
        draw_box(0)
        draw_arrow((0,255,0))
        draw_exit((255,255,255))
     
    def menu_x_quit():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_winmenu((255,255,255))
        draw_x((255,255,255))
        draw_box(13)
        draw_arrow((255,255,255))
        draw_exit((255,0,0))

    def menu_o_play():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_winmenu((255,255,255))
        draw_o((255,255,255))
        draw_box(0)
        draw_arrow((0,255,0))
        draw_exit((255,255,255))
    
    def menu_o_quit():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_winmenu((255,255,255))
        draw_o((255,255,255))
        draw_box(13)
        draw_arrow((255,255,255))
        draw_exit((255,0,0))
    
    def menu_tie_play():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_tiemenu((255,255,255))
        draw_box(0)
        draw_arrow((0,255,0))
        draw_exit((255,255,255))

    def menu_tie_quit():
        draw.rectangle((0,0,31,31),fill=(0,0,0))
        draw_tiemenu((255,255,255))
        draw_box(13)
        draw_arrow((255,255,255))
        draw_exit((255,0,0))

    while running:

        if joystick_found:
            if joystick.get_button(10):
                running = False 
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            if not(winner in [0,1,2]):
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
        if winner == -1:
            if joystick.get_button(8) and ((x,y) not in player_x and (x,y) not in player_circle) and len(player_circle) <= len(player_x) and game_over == False and player == 0 and (initial_input_delay <= 0):
                player_circle.add((x,y))
                player = 1
            if joystick.get_button(8) and ((x,y) not in player_x and (x,y) not in player_circle) and (len(player_circle) > len(player_x)) and game_over == False and player == 1 and (initial_input_delay <= 0):
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

            ##print(x)
            ##print(y)

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
                #print("h1")
                winner = 0
                game_over = True
            elif (1*scale,11*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,11*scale) in player_circle :
                #print("h2")
                winner = 0
                game_over = True
            elif (1*scale,21*scale) in player_circle and (11*scale,21*scale) in player_circle and (21*scale,21*scale) in player_circle :
                #print("h3")
                winner = 0
                game_over = True
            #Vertical
            elif (1*scale,1*scale) in player_circle and (1*scale,11*scale) in player_circle and (1*scale,21*scale) in player_circle :
                #print("v1")
                winner = 0
                game_over = True
            elif (11*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (11*scale,21*scale) in player_circle :
                #print("v2")
                winner = 0
                game_over = True
            elif (21*scale,1*scale) in player_circle and (21*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
                #print("v3")
                winner = 0
                game_over = True
            #Diogonal
            elif (1*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
                #print("d1")
                winner = 0
                game_over = True
            elif (1*scale,21*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,1*scale) in player_circle :
                #print("d2")
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
                #print("tie1")
                winner = 2
                game_over = True
            elif len(player_circle) == 4 and len(player_x) == 5:
                #print("tie2")
                winner = 2
                game_over = True

        elif winner == -2:
            game_over = False
            player= 0
            player_circle = set([])
            player_x = set([])
            input_lock_time = 0.3
            last_input_time = 0
            initial_input_delay = 0.3
            winner = -1
            menu_delay = 0.3
            menu_move_value = -1
            dt = 0
            x = 11
            y = 1
            # time.sleep(0.3)
        
        if winner in [0,1,2]:
            menu_delay = menu_delay -dt
            menu_move_value = menu_movement(joystick,menu_move_value)
        # if joystick.get_button(8):
            # #print("main:button8:",joystick.get_button(8))
            # #print("main:move_value",menu_move_value)
        
            if menu_move_value == -1:
                if joystick.get_button(8) and menu_delay < 0:
                    #print("main:reset")
                    winner = -2
                    menu_move_value = 0
                if winner == 0:
                    menu_o_play()
                elif winner == 1:
                    menu_x_play()
                elif winner == 2:
                    menu_tie_play()

            elif menu_move_value == 1:
                if joystick.get_button(8) and menu_delay < 0:
                    #print("main:quit tiktatktoe")
                    running = False
                if winner == 0:
                    menu_o_quit()
                elif winner == 1:
                    menu_x_quit()
                elif winner == 2:
                    menu_tie_quit()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
                running = False  # ends pygamgesz

        # #print("main:jbutton8:", joystick.get_button(8))
        # #print("main:jbutton9:", joystick.get_button(9))
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60)/1000