from lose_menu import start_losemenu


def start_snake(matrix, joystick_found, joystick, draw, image):
    import pygame
    import random
    import copy
    screen_width = 31
    screen_height = 31
    clock = pygame.time.Clock()

    SPEED = 1
    tail = []
    clist = []

    global score
    global snake_dir
    global apple
    global running
    score = 0
    snake_dir = (0, 1)
    apple = 0
    running = True

    def spawn_snake():
        for i in range(0, 6):
            x = pygame.Rect(i , 0, 1 , 1 )
            tail.append(x)
            clist.append(x)

    def spawn_apple():
        # while not on element from tail
        snake_points = [(e.left, e.top) for e in tail]
        x = random.randint(0, 31)
        y = random.randint(0, 31)
        while (x, y) in snake_points:
            x = random.randint(0, 31)
            y = random.randint(0, 31)
        return pygame.Rect(x , y , 1, 1)

    def move_snake_joy(x_axis, y_axis, threshold=0.1):
        global snake_dir
        # Schwellenwert für Stick-Drift oder Neutralzone
        x_axis = 0 if abs(x_axis) < threshold else x_axis
        y_axis = 0 if abs(y_axis) < threshold else y_axis
        if x_axis < 0 and snake_dir != (-1, 0):
            snake_dir = (1, 0)
        elif x_axis > 0 and snake_dir != (1, 0):
            snake_dir = (-1, 0)
        elif y_axis < 0 and snake_dir != (0, -1):
            snake_dir = (0, 1)
        elif y_axis > 0 and snake_dir != (0, 1):
            snake_dir = (0, -1)

        for i in range(0, len(tail) - 1):
            tail[i + 1] = copy.deepcopy(clist[i])

        tail[0].move_ip(SPEED * snake_dir[0], SPEED * snake_dir[1])
        for i, e in enumerate(tail):
            clist[i] = copy.deepcopy(tail[i])

    def move_snake():
        global snake_dir
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and snake_dir != (0, 1):
            snake_dir = (0, -1)
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and snake_dir != (1, 0):
            snake_dir = (-1, 0)
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and snake_dir != (0, -1):
            snake_dir = (0, 1)
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and snake_dir != (-1, 0):
            snake_dir = (1, 0)
        for i in range(0, len(tail) - 1):
            tail[i + 1] = copy.deepcopy(clist[i])

        tail[0].move_ip(SPEED * snake_dir[0], SPEED * snake_dir[1])
        for i, e in enumerate(tail):
            clist[i] = copy.deepcopy(tail[i])

    def check_events():
        global snake_dir, apple, score, running
        # collision border
        for i in range(1, len(tail) - 1):
            if (tail[0].left == tail[i].left) and tail[0].top == tail[i].top:
                running = False
        if (tail[0].left < 0) or (tail[0].left > screen_width) or (tail[0].top < 0) or (tail[0].top > screen_height):
            running = False

        # snake on apple
        if tail[0].left == apple.left and tail[0].top == apple.top:
            apple = spawn_apple()
            score = score + 1
            tail.append(tail[len(tail) - 1].move(SPEED * snake_dir[0], -SPEED * snake_dir[1]))
            clist.append(tail[len(tail) - 1].move(SPEED * snake_dir[0], -SPEED * snake_dir[1]))

    spawn_snake()
    apple = spawn_apple()

    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

        # clear screen
        draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0))
        if joystick_found:
            if joystick.get_button(10):
                running = False
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            move_snake_joy(x_axis, y_axis)
        else:
            move_snake()
        check_events()

        # Drawing Snake and Apple
        if tail:
            head = tail[0]
            draw.point((head.left, head.top), (255, 0, 0))

        for e in tail[1:]:
            draw.point((e.left, e.top), (0, 255, 255))

        draw.point((apple.left, apple.top), (255, 255, 0))

        matrix.SetImage(image, 0, 0)
        dt = clock.tick(8) / 1000

    return {"score": score, "game": "snake"}
