import pygame
import time

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
    RED = (255,0,0)
    BLUE = (0,0,255)
    BORDER_COLOR = WHITE

    # defining the moving rectangle
    x = 11   # start position
    y = 1
    grid_point_spacing = 10  # distance between points of the 3x3 grid

    clock = pygame.time.Clock()
    running = True
    active_player = 0

    #Tuple to write positions x and y
    player_o = set([])
    player_x = set([])

    # winner as state of the game
    # winner = -2: resetting the game vars
    # winner = -1: normal game loop
    # winner = 0: o wins
    # winner = 1: x wins
    winner = -1

    def menu_movement(joystick,value):
        x_axis = joystick.get_axis(0)
        if x_axis > 0.1:
            value = -1
        elif x_axis < -0.1:
            value = 1
        return value

    def draw_lines(lines, color):
        for line_cords in lines:
            draw.line(line_cords,fill=color)

    def draw_points(points,color):
        for point_cords in points:
            draw.point(point_cords,fill=color)

    def draw_rectangles(rectangles,color):
        for rectangle_cords in rectangles:
            draw.rectangle(rectangle_cords,fill=color)

    def draw_tiemenu(text_color):
        # Draw TIE and its underline using lines
        lines = [
            (7, 1, 13, 1),(10, 1, 10, 7),(16, 1, 16, 7),(19, 1, 19, 7),
            (19, 1, 24, 1),(19, 4, 23, 4),(19, 7, 24, 7),(1, 9, 30, 9),
            (1, 7, 1, 9),(30, 7, 30, 9)
        ]
        draw_lines(lines,text_color)

    def draw_x(color):
        lines=[(3,3,7,7),(7,3,3,7)]
        draw_lines(lines,color)

    def draw_o(color):
        #draws o
        draw.ellipse((3,3,7,7), fill=(color))
        draw.rectangle((4,4,6,6), fill=(BLACK))

    def draw_winmenu(text_color):
        # Draw WIN using lines and points
        lines = [
            (11, 3, 11, 7),(15, 3, 15, 7),(17, 3, 17, 7),(19, 3, 19, 7),
            (20, 4, 20, 4),(21, 5, 21, 5),(22, 6, 22, 6),(23, 3, 23, 7),
            (25, 3, 28, 3),(25, 5, 28, 5),(25, 7, 28, 7),(1, 9, 30, 9),
            (1, 7, 1, 9),(30, 7, 30, 9)
        ]
        points = [
            (12, 6),(13, 5),(14, 6),(25, 4),(28, 6)
        ]

        draw_lines(lines,text_color)
        draw_points(points,text_color)

    def draw_box(x):
        #draws box for play arrow
        rectangles = [(5+x,11,5+x,21),(5+x,11,13+x,11),(13+x,11,13+x,21),(5+x,21,13+x,21)]
        draw_rectangles(rectangles,BORDER_COLOR)

    def draw_arrow(color):
        #draws arrow
        rectangles=[(8,14,8,18),(9,15,9,17),(10,16,10,16)]
        draw_rectangles(rectangles,color)

    def draw_exit(color):
        # Points for drawing 'X'
        points = [(20, 14), (21, 15), (22, 16), (23, 17), (24, 18), (20, 18), (21, 17), (22, 16), (23, 15), (24, 14)]
        draw_points(points,color)

    def move_box_joy(x_axis, y_axis, threshold=0.1):
        global last_input_time
        global input_lock_time
        global y
        global x

        current_time=time.time()
        if current_time - last_input_time <= input_lock_time:
            return
        # Schwellenwert für Stick-Drift oder Neutralzone
        x_axis = 0 if abs(x_axis) < threshold else x_axis
        y_axis = 0 if abs(y_axis) < threshold else y_axis
        last_input_time = current_time
        if x_axis < 0 and x < 21:
            x += grid_point_spacing
        elif x_axis > 0 and x > 1:
            x -= grid_point_spacing
        elif y_axis < 0 and y < 21:
            y += grid_point_spacing
        elif y_axis > 0 and y > 1:
            y -= grid_point_spacing

    def draw_board():
        squares = [
            (2, 2, 9, 9), (12, 2, 19, 9), (22, 2, 29, 9),
            (2, 12, 9, 19), (12, 12, 19, 19), (22, 12, 29, 19),
            (2, 22, 9, 29), (12, 22, 19, 29), (22, 22, 29, 29)
        ]
        draw.rectangle((0, 0, 32, 32), fill=WHITE)
        draw_rectangles(squares,BLACK)

    def draw_menu(draw_shape, box_offset, arrow_color, exit_color):
        draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0))
        draw_winmenu((255, 255, 255))
        draw_shape((255, 255, 255))
        draw_box(box_offset)
        draw_arrow(arrow_color)
        draw_exit(exit_color)

    def menu_x_play():
        draw_menu(draw_x, 0, (0, 255, 0), (255, 255, 255))

    def menu_x_quit():
        draw_menu(draw_x, 13, (255, 255, 255), (255, 0, 0))

    def menu_o_play():
        draw_menu(draw_o, 0, (0, 255, 0), (255, 255, 255))

    def menu_o_quit():
        draw_menu(draw_o, 13, (255, 255, 255), (255, 0, 0))

    def menu_tie_play():
        draw_menu(draw_tiemenu, 0, (0, 255, 0), (255, 255, 255))

    def menu_tie_quit():
        draw_menu(draw_tiemenu, 13, (255, 255, 255), (255, 0, 0))

    def draw_player_o(player_cords):
        for p_x,p_y in player_cords:
            draw.ellipse((p_x+1,p_y+1,p_x+8,p_y+8),fill=BLUE)
            draw.ellipse((p_x+2,p_y+2,p_x+7,p_y+7),fill=BLACK)

    def draw_player_x(player_cords):
        for p_x,p_y in player_cords:
            draw.line((p_x+1, p_y+1, p_x+8, p_y+8),fill=RED)
            draw.line((p_x+1, p_y+8, p_x+8, p_y+1),fill=RED)

    # Define winning combinations
    winning_combinations = [
        # Horizontal
        [(1, 1), (11, 1), (21, 1)],
        [(1, 11), (11, 11), (21, 11)],
        [(1, 21), (11, 21), (21, 21)],
        # Vertical
        [(1, 1), (1, 11), (1, 21)],
        [(11, 1), (11, 11), (11, 21)],
        [(21, 1), (21, 11), (21, 21)],
        # Diagonal
        [(1, 1), (11, 11), (21, 21)],
        [(1, 21), (11, 11), (21, 1)]
    ]

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
            if keys[pygame.K_LEFT] and x > 1 :
                x -= grid_point_spacing
            if keys[pygame.K_RIGHT] and x < 21 :
                x += grid_point_spacing
            if keys[pygame.K_UP] and y > 1 :
                y -= grid_point_spacing
            if keys[pygame.K_DOWN] and y < 21 :
                y += grid_point_spacing


        # player_x or player_o -sign is placed
        if winner == -1:
            if ((joystick_found and joystick.get_button(8)) or (keys[pygame.K_SPACE]) ) and ((x,y) not in player_x and (x,y) not in player_o) and (initial_input_delay <= 0):
                if active_player == 0:
                    player_o.add((x,y))
                    active_player = 1
                elif active_player == 1:
                    player_x.add((x,y))
                    active_player = 0

            # Drawing:
            draw_board()
            # moving rectangle
            active_player_color = BLUE if active_player == 0 else RED
            draw.rectangle((x ,y ,x+9,y+9),fill=active_player_color)
            draw.rectangle((x+1 ,y+1 ,x+8,y+8),fill=BLACK)

            draw_player_o(player_o)
            draw_player_x(player_x)

            # Check for win for both players
            for player in [player_o, player_x]:
                for combination in winning_combinations:
                    if all(pos in player for pos in combination):
                        winner = 0 if player == player_o else 1
                        break
                if winner in [0,1]:
                    break

            # Check for tie
            if (len(player_o) + len(player_x)) == 9:
                winner = 2

        # resetting all game states:
        elif winner == -2:
            active_player = 0
            player_o = set([])
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

        if winner in [0,1,2]:
            menu_delay = menu_delay - dt
            menu_move_value = menu_movement(joystick,menu_move_value)
            if menu_move_value == -1:
                if joystick.get_button(8) and menu_delay < 0:
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
                    running = False
                if winner == 0:
                    menu_o_quit()
                elif winner == 1:
                    menu_x_quit()
                elif winner == 2:
                    menu_tie_quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        initial_input_delay = initial_input_delay-dt
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60)/1000