def start_losemenu(matrix, joystick_found, joystick, draw, image, game_data):
    import pygame
    import time
    from displaying_characters import display_chars
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BORDER_COLOR = WHITE

    RETURN = 8
    global option
    option = "EXIT"
    global x
    x = 0
    global play_color, exit_color, save_color
    play_color = (GREEN)
    exit_color = (WHITE)
    save_color = (WHITE)
    global running
    running = True

    def draw_box(x):
        # draws box for play arrow
        draw.rectangle((2 + x, 11, 2 + x, 21), fill=(BORDER_COLOR))
        draw.rectangle((2 + x, 11, 10 + x, 11), fill=(BORDER_COLOR))
        draw.rectangle((10 + x, 11, 10 + x, 21), fill=(BORDER_COLOR))
        draw.rectangle((2 + x, 21, 10 + x, 21), fill=(BORDER_COLOR))

    def draw_arrow(color):
        # draws arrow
        draw.rectangle((5, 14, 5, 18), fill=(color))
        draw.rectangle((6, 15, 6, 17), fill=(color))
        draw.rectangle((7, 16, 7, 16), fill=(color))

    def draw_exit(color):
        # draws x
        draw.point((24, 15), fill=(color))
        draw.point((25, 16), fill=(color))
        draw.point((26, 17), fill=(color))
        draw.point((27, 18), fill=(color))
        draw.point((28, 19), fill=(color))
        draw.point((24, 19), fill=(color))
        draw.point((25, 18), fill=(color))
        draw.point((26, 17), fill=(color))
        draw.point((27, 16), fill=(color))
        draw.point((28, 15), fill=(color))


    def move_box():
        global x
        global running
        global option
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:  # movement of the select box
            x -= 20
        if keys[pygame.K_RIGHT] and x <= 10:
            x += 20

        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            if x == 0:
                option = "PLAY"
            if x == 20:
                option = "EXIT"
            running = False

    def set_color():
        global play_color
        global exit_color
        global save_color
        global x
        # sets the colors for the content of the boxes
        if x == 0:
            play_color = (GREEN)
            save_color = (WHITE)
            exit_color = (WHITE)
        if x == 20:
            play_color = (WHITE)
            save_color = (WHITE)
            exit_color = (RED)

    def move_box_joy(x_axis):
        global x
        global running
        global option
        threshold = 0.1

        x_axis = 0 if abs(x_axis) < threshold else x_axis
        if x_axis > 0 and x > 0:
            x -= 20
        elif x_axis < 0 and x < 20:
            x += 20

        if joystick.get_button(RETURN):
            if x == 0:
                option = "PLAY"
            if x == 20:
                option = "EXIT"
            running = False

    clock = pygame.time.Clock()  # is just a clock for how often the while loop is repeated
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if joystick_found:
            x_axis = joystick.get_axis(0)
            move_box_joy(x_axis)
        else:
            move_box()
        set_color()
        draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0, 0))
        draw_box(x)
        draw_arrow(play_color)
        draw_exit(exit_color)

        display_chars(str(game_data["score"]), 2, (32 - 4 * len(str(game_data["score"]))) // 2, draw)

        matrix.SetImage(image, 0, 0)
        clock.tick(60)

    return option
