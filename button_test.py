import pygame
import time

def start_button_test(matrix, joystick_found, joystick, draw, image):
    pygame.init()
    running = True
    
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def draw_button_8():
        draw.line((6, 8, 8, 8), fill=BLUE)
        draw.line((5, 9, 5, 11), fill=BLUE)
        draw.line((9, 9, 9, 11), fill=BLUE)
        draw.line((6, 12, 8, 12), fill=BLUE)

    def draw_button_9():
        draw.line((10, 13, 12, 13), fill=YELLOW)
        draw.line((13, 14, 13, 16), fill=YELLOW)
        draw.line((10, 17, 12, 17), fill=YELLOW)
        draw.line((9, 14, 9, 16), fill=YELLOW)

    def draw_button_10():
        draw.line((2, 13, 4, 13), fill=YELLOW)
        draw.line((5, 14, 5, 16), fill=YELLOW)
        draw.line((2, 17, 4, 17), fill=YELLOW)
        draw.line((1, 14, 1, 16), fill=YELLOW)

    def draw_button_11():
        draw.line((6, 18, 8, 18), fill=BLUE)
        draw.line((9, 19, 9, 21), fill=BLUE)
        draw.line((5, 19, 5, 21), fill=BLUE)
        draw.line((6, 22, 8, 22), fill=BLUE)

    def draw_joystick_up(color):
        draw.line((24, 9, 24, 13), fill=color)
        draw.line((22, 11, 24, 9), fill=color)
        draw.line((24, 9, 26, 11), fill=color)

    def draw_joystick_left(color):
        draw.line((18, 15, 22, 15), fill=color)
        draw.line((18, 15, 20, 13), fill=color)
        draw.line((18, 15, 20, 17), fill=color)

    def draw_joystick_right(color):
        draw.line((26, 15, 30, 15), fill=color)
        draw.line((28, 13, 30, 15), fill=color)
        draw.line((28, 17, 30, 15), fill=color)

    def draw_joystick_down(color):
        draw.line((24, 17, 24, 21), fill=color)
        draw.line((22, 19, 24, 21), fill=color)
        draw.line((24, 21, 26, 19), fill=color)

    def joystick_inputs(x_axis, y_axis, exit_timer, threshold=0.1):
        x_axis = 0 if abs(x_axis) < threshold else x_axis
        y_axis = 0 if abs(y_axis) < threshold else y_axis
        if x_axis < 0:
            draw_joystick_right(WHITE)
            exit_timer = 5
        if x_axis > 0:
            draw_joystick_left(WHITE)
            exit_timer = 5
        if y_axis < 0:
            draw_joystick_down(WHITE)
            exit_timer = 5
        if y_axis > 0:
            draw_joystick_up(WHITE)
            exit_timer = 5

        if joystick.get_button(8):
            draw.rectangle((10, 14, 12, 16), fill=YELLOW)
            exit_timer = 5
        if joystick.get_button(9):
            draw.rectangle((6, 9, 8, 11), fill=BLUE)
            exit_timer = 5
        if joystick.get_button(10):
            draw.rectangle((2, 14, 4, 16), fill=YELLOW)
            exit_timer = 5
        if joystick.get_button(11):
            draw.rectangle((6, 19, 8, 21), fill=BLUE)
            exit_timer = 5
        return exit_timer

    exit_timer = 5
    dt = 0
    clock = pygame.time.Clock()
    while running:
        if exit_timer < 0:
            running = False
        pygame.event.get()
        draw.rectangle((0, 0, 31, 31), fill=BLACK)
        draw_button_8()
        draw_button_9()
        draw_button_10()
        draw_button_11()
        draw_joystick_up(GREY)
        draw_joystick_left(GREY)
        draw_joystick_right(GREY)
        draw_joystick_down(GREY)

        if joystick_found:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            exit_timer = joystick_inputs(x_axis, y_axis, exit_timer)
        exit_timer = exit_timer - dt
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60)/1000
