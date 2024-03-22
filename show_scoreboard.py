from displaying_characters import display_chars
from scoreboard import Scoreboard
import pygame
import time
def start_show_scoreboard(matrix, joystick_found, joystick, draw, image):
    pygame.init()

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    RED = (255,0,0)
    YELLOW = (255,221,0)
    GREEN = (0,255,0)
    GREY = (128,128,128)
    DARK_GREY = (64,64,64)
    LIGHT_GREY = (192,192,192)
    GOLD = (212,175,55)

    RETURN = 8

    global last_input_time, running,input_lock_time, position_x, position_y
    position_x = 15
    position_y = 15
    running = True

    input_lock_time = .5
    last_input_time = 0

    clock = pygame.time.Clock()

    def display_scoreboard(game, draw, scoreboard):

        placements = scoreboard.get_placement_ranging(game,1,5)
        place = 1
        for name,score in placements:
            y_cords = 6*(place-1)
            display_chars(str(place)+" "+ str(score),y_cords, 1,draw)
            place = place+1

    def draw_grid():
        draw.rectangle((15, 0, 16, 31), fill=GOLD)
        draw.rectangle((0, 15, 31, 16), fill=GOLD)

    def draw_pong(wall_color, ball_color):
        draw.line((0,2,0,5), fill=wall_color)
        draw.line((14,0,14,14), fill=wall_color)
        draw.point((7,5), fill=ball_color)

    def draw_snake(body_color, head_color, apple_color):
        draw.line((18,3,18,6), fill=body_color)
        draw.line((18,6,21,6), fill=body_color)
        draw.line((21,6,21,11), fill=body_color)
        draw.line((21,11,24,11), fill=body_color)
        draw.point((25,11), fill=head_color)
        draw.point((28,4), fill=apple_color)

    def draw_space_invaders(mob_color, rock_color, bullet_color, player_color, base_color):

        draw.rectangle((2,18,3,19), fill=mob_color)
        draw.rectangle((5,18,6,19), fill=mob_color)
        draw.rectangle((8,18,9,19), fill=mob_color)
        draw.rectangle((11,18,12,19), fill=mob_color)
        draw.rectangle((2,21,3,22), fill=mob_color)
        draw.rectangle((5,21,6,22), fill=mob_color)
        draw.rectangle((8,21,9,22), fill=mob_color)
        draw.rectangle((11,21,12,22), fill=mob_color)
        draw.rectangle((2,24,3,25), fill=mob_color)
        draw.rectangle((8,24,9,25), fill=mob_color)
        draw.rectangle((11,24,12,25), fill=mob_color)

        draw.rectangle((2,27,3,28), fill=rock_color)
        draw.point((3,28), fill=BLACK)
        draw.rectangle((8,27,9,28), fill=rock_color)
        draw.point((8,27), fill=BLACK)
        draw.rectangle((11,27,12,28), fill=rock_color)
        draw.point((11,28), fill=BLACK)

        draw.line((5,26,5,27), fill=bullet_color)

        draw.line((4,30,6,30), fill=player_color)
        draw.line((0,31,14,31), fill=base_color)

    def draw_runner(player_color, border_color, obstacle_color):
        draw.point((19,30),fill=player_color)

        draw.line((17,17,31,17), fill=border_color)
        draw.line((17,31,31,31), fill=border_color)

        draw.point((23,21), fill=obstacle_color)
        draw.point((25,25), fill=obstacle_color)
        draw.point((28,29), fill=obstacle_color)
        draw.point((28,18), fill=obstacle_color)
        draw.point((31,30), fill=obstacle_color)

    def move_joy(x_axis, y_axis,game_displayed,exiting_timer):
        global position_x
        global position_y
        global running
        global last_input_time
        global input_lock_time

        current_time = time.time()
        threshold = 0.1

        if current_time - last_input_time > input_lock_time:
            x_axis = 0 if abs(x_axis) < threshold else x_axis
            y_axis = 0 if abs(y_axis) < threshold else y_axis
            if x_axis < 0:
                if position_x < 20:
                    position_x += 15
                    last_input_time = current_time
            elif x_axis > 0:
                if position_x > 20:
                    position_x -= 15
                    last_input_time = current_time
            elif y_axis < 0:
                if position_y < 20:
                    position_y += 15
                    last_input_time = current_time
            elif y_axis > 0:
                if position_y > 20:
                    position_y -= 15
                    last_input_time = current_time

            if joystick.get_button(RETURN):
                if position_x < 20:
                    if position_y < 20:
                        game_displayed="pong"
                    if position_y > 20:
                        game_displayed="space_invaders"
                if position_x > 20:
                    if position_y < 20:
                        game_displayed="snake"
                    if position_y > 20:
                        game_displayed="runner"

            if joystick.get_button(10) and game_displayed == "" and exiting_timer <= 0:
                running = False
            elif joystick.get_button(10):
                game_displayed=""
                exiting_timer = 0.3

        return game_displayed,exiting_timer

    def draw_colored(position_x, position_y):
        if position_x < 20:
            if position_y < 20:
                draw_pong(WHITE, RED)
            if position_y > 20:
                draw_space_invaders(RED, GREY, LIGHT_GREY, GREEN, YELLOW)
        if position_x > 20:
            if position_y < 20:
                draw_snake(BLUE, RED, YELLOW)
            if position_y > 20:
                draw_runner(BLUE, WHITE, RED)

    def draw_grey():
        draw_pong(LIGHT_GREY, GREY)
        draw_snake(GREY, DARK_GREY, LIGHT_GREY)
        draw_space_invaders(GREY, DARK_GREY, LIGHT_GREY, LIGHT_GREY, GREY)
        draw_runner(LIGHT_GREY, GREY, DARK_GREY)

    scoreboard = Scoreboard()
    scoreboard.read_from_file("score.json")
    game_displayed = ""
    scoreboard_keys = scoreboard.get_games()
    exiting_timer = 0
    dt = 0
    initial_timer = 0.3
    while running:
        pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if joystick_found:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            if initial_timer < 0:
                game_displayed,exiting_timer = move_joy(x_axis,y_axis,game_displayed,exiting_timer)

        draw.rectangle((0, 0, 31, 31), BLACK)
        if game_displayed == "pong" and "pong" in scoreboard_keys:
            display_scoreboard("pong",draw,scoreboard)
        elif game_displayed == "snake" and "snake" in scoreboard_keys:
            display_scoreboard("snake",draw,scoreboard)
        elif game_displayed == "space_invaders" and "space_invaders" in scoreboard_keys:
            display_scoreboard("space_invaders",draw,scoreboard)
        elif game_displayed == "runner" and "runner" in scoreboard_keys:
            display_scoreboard("runner",draw,scoreboard)
        else:
            draw_grid()
            draw_grey()
            draw_colored(position_x, position_y)

        matrix.SetImage(image)
        exiting_timer = exiting_timer-dt
        initial_timer = initial_timer-dt
        dt = clock.tick(60) / 1000