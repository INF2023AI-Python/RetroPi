import pygame
import random
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

pygame.init()

WIDTH = 32
HEIGHT = 32
SCALE = 1
TOP_FLOOR = 13
BOTTOM_FLOOR = 29

player_x = 3*SCALE
player_y = (BOTTOM_FLOOR-1)*SCALE
y_change = 0
gravity = 1
score = 0
speedaddition = 0
running = True

obstacles = []

try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

def draw_floor():
    draw.rectangle((0,BOTTOM_FLOOR,32,BOTTOM_FLOOR),fill=(255,255,255))
    draw.rectangle((0,TOP_FLOOR,32,TOP_FLOOR),fill=(255,255,255))

def spawn_random_obstacle():
    obstacle_x = (WIDTH-1)*SCALE
    obstacle_y = random.randint(TOP_FLOOR+1, BOTTOM_FLOOR-1)*SCALE
    obstacles.append((obstacle_x, obstacle_y))

def spawn_fixed_obstacle():
    obstacle_x = (WIDTH-1)*SCALE
    obstacle_y = BOTTOM_FLOOR-1*SCALE
    obstacles.append((obstacle_x, obstacle_y))
    obstacle_x = (WIDTH-1)*SCALE
    obstacle_y = TOP_FLOOR+1*SCALE
    obstacles.append((obstacle_x, obstacle_y))

def draw_obstacles():
    for obstacle in obstacles:
        draw.rectangle((obstacle[0],obstacle[1],obstacle[0],obstacle[1]),fill=(255,0,0))

def collision(): #just checks for a collision from the front
    for obstacle in obstacles:
        if player_x <= obstacle[0] <= player_x + SCALE and player_y <= obstacle[1] <= player_y + SCALE:
            return True
    return False

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gravity > 0:
                    gravity = -1
                    y_change = 1
                else:
                    gravity = 1
                    y_change = -1
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick Button pressed")
            if event.button == 8:
                if gravity > 0:
                    gravity = -1
                    y_change = 1
                else:
                    gravity = 1
                    y_change = -1

    if player_y < (BOTTOM_FLOOR-1)*SCALE or y_change > 0 or player_y > (TOP_FLOOR+1)*SCALE:
        player_y -= y_change
        y_change -= gravity
    if gravity > 0 and player_y > (BOTTOM_FLOOR-1)*SCALE:
        player_y = (BOTTOM_FLOOR-1)*SCALE
        y_change = 0
    if gravity < 0 and player_y < (TOP_FLOOR+1)*SCALE:
        player_y = (TOP_FLOOR+1)*SCALE
        y_change = 0


    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw.rectangle((player_x, player_y, player_x, player_y), fill=(255, 255, 255))
    draw_floor()
    draw_obstacles()
    matrix.SetImage(image, 0, 0)

    if random.randint(0, 100) < 10:
        if random.randint(0, 100) < 75:
            spawn_random_obstacle()
        else:
             spawn_fixed_obstacle()

    obstacles = [(x-SCALE, y) for x, y in obstacles if x > 0]

    if collision():
        print("Game Over")
        running = False

    score += 1
    print(score)

    if random.randint(0, 100) < 1:
        speedaddition += 1
    pygame.time.delay(1000//10+speedaddition)
pygame.quit()