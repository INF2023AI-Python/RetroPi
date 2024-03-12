import pygame
import random
import copy
from PIL import Image
from PIL import ImageDraw

try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

running = True
joystick_found = True
SCALE = 1
pygame.init()
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

screen_width = 32 * SCALE
screen_height = 32 * SCALE
clock = pygame.time.Clock()

SPEED = 1
tail = []
clist = []

global score
score = 0

global snake_dir
snake_dir = (0, 1)

global apple
apple = 0


def spawn_snake():
    for i in range(0, 10):
        x = pygame.Rect(i * SCALE, 0, 1 * SCALE, 1 * SCALE)
        tail.append(x)
        clist.append(x)


def spawn_apple():
    # while not on element from tail
    snake_points = [(e.left,e.top) for e in tail]
    x = random.randint(0, 31)
    y = random.randint(0, 31)
    while (x,y) in snake_points:
        x = random.randint(0, 31)
        y = random.randint(0, 31)

    return pygame.Rect(x * SCALE, y * SCALE, SCALE, SCALE)


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
    if keys[pygame.K_w] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    elif keys[pygame.K_a] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    elif keys[pygame.K_s] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    elif keys[pygame.K_d] and snake_dir != (-1, 0):
        snake_dir = (1, 0)
    for i in range(0, len(tail) - 1):
        tail[i + 1] = copy.deepcopy(clist[i])

    tail[0].move_ip(SPEED * snake_dir[0], SPEED * snake_dir[1])
    for i, e in enumerate(tail):
        clist[i] = copy.deepcopy(tail[i])


def check_events():
    global snake_dir, apple, score
    # collision with border directions are relative
    next_position_ahead = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])
    next_position_left = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])
    next_position_right = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])

    # split into method for other checks, such as left and right relative from the snake for self collision
    if collision_self(next_position_ahead):
        print("dead self")
    if collision_self(next_position_left):
        print("dead left")
    if collision_self(next_position_right):
        print("dead right")

    # collision ahead
    if (next_position_ahead.left < 0) or (next_position_ahead.left > screen_width) or (next_position_ahead.top < 0) or (
            next_position_ahead.top > screen_height):
        print("dead border")
    # collision above
    # collsion below

    # snake on apple
    if tail[0].left == apple.left and tail[0].top == apple.top:
        apple = spawn_apple()
        score = score + 1
        tail.append(tail[len(tail) - 1].move(SPEED * snake_dir[0], -SPEED * snake_dir[1]))
        clist.append(tail[len(tail) - 1].move(SPEED * snake_dir[0], -SPEED * snake_dir[1]))
        print("len tail: ", len(tail))
        print(score)


def collision_self(next_relative_position: pygame.Rect) -> bool:
    for snake_element in tail:
        if snake_element.left == next_relative_position.left and snake_element.top == next_relative_position.top:
            return True
    return False


spawn_snake()
apple = spawn_apple()

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you hjve an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0, 0))
    if joystick_found:
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)
        move_snake_joy(x_axis, y_axis)


    move_snake()
    check_events()
    head = tail[0]
    for i, e in enumerate(tail):
        if i == 0:
            draw.rectangle((head.left, head.top, head.left, head.top), fill=(255, 0, 0))
        else:
            draw.rectangle((e.left, e.top, e.left, e.top), fill=(0, 255, 255))

    print(head.left, head.top)
    draw.rectangle((apple.left, apple.top, apple.left, apple.top), fill=(255, 255, 0))

    matrix.SetImage(image, 0, 0)
    dt = clock.tick(8) / 1000
pygame.quit()
