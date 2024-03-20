import pygame
import random
import math
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

player_x = 3
player_y = (BOTTOM_FLOOR-1)
y_change = 0
gravity = 1
score = 0
speedaddition = 0
SPEED = 0.2
obstacle_speed = SPEED
# obstacle_speed velo
dt = 0
running = True
clock = pygame.time.Clock()

obstacles = []

try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

def temp_get_dist(obstacle,player_x,player_y):
    x_distance = obstacle[0]-player_x
    y_distance = obstacle[1]-player_y
    distance = math.sqrt(x_distance*x_distance + y_distance*y_distance)
    return distance

def draw_floor():
    draw.rectangle((0,BOTTOM_FLOOR,32,BOTTOM_FLOOR),fill=(255,255,255))
    draw.rectangle((0,TOP_FLOOR,32,TOP_FLOOR),fill=(255,255,255))

def spawn_random_obstacle():
    obstacle_x = (WIDTH-1)
    obstacle_y = random.randint(TOP_FLOOR+1, BOTTOM_FLOOR-1)
    obstacles.append((obstacle_x, obstacle_y))

def spawn_fixed_obstacle():
    obstacle_x = (WIDTH-1)
    obstacle_y = BOTTOM_FLOOR-1
    obstacles.append((obstacle_x, obstacle_y))
    obstacle_x = (WIDTH-1)
    obstacle_y = TOP_FLOOR+1
    obstacles.append((obstacle_x, obstacle_y))

def draw_obstacles():
    for obstacle in obstacles:
        draw.rectangle((obstacle[0],obstacle[1],obstacle[0],obstacle[1]),fill=(255,0,0))

def collision(): #just checks for a collision from the front
    for obstacle in obstacles:
        # if player_x <= obstacle[0] <= player_x + SCALE and player_y <= obstacle[1] <= player_y + SCALE:
        # if player_x <= obstacle[0] <= player_x and player_y <= obstacle[1] <= player_y :
        if int(player_x) == int(obstacle[0]) and int(player_y) == int(obstacle[1]):
            return True
    return False

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)
spawn_timer = 0

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

    if player_y < (BOTTOM_FLOOR-1) or y_change > 0 or player_y > (TOP_FLOOR+1):
        player_y -= y_change*SPEED
        y_change -= gravity
    if gravity > 0 and player_y > (BOTTOM_FLOOR-1):
        player_y = (BOTTOM_FLOOR-1)
        y_change = 0
    if gravity < 0 and player_y < (TOP_FLOOR+1):
        player_y = (TOP_FLOOR+1)
        y_change = 0

    obstacles = [(x-obstacle_speed, y) for x, y in obstacles if x > 0]
    for obstacle in obstacles:
        distance = temp_get_dist(obstacle,player_x,player_y)
        if distance <= 2:
            print(distance)
        if distance <= 1:
            running = False
            print("Lost")
            # print(distance)

    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw.rectangle((player_x, player_y, player_x, player_y), fill=(255, 255, 255))
    draw_floor()
    draw_obstacles()
    matrix.SetImage(image, 0, 0)

    if spawn_timer <= 0:
        spawn_timer = 0.85
        # if random.randint(0, 100) < 33:
        spawn_random_obstacle()
    else:
        spawn_timer = spawn_timer - dt
    

    # if collision():
    #     print("Game Over")
    #     running = False

    score += dt
    # print(int(score)) 

    # if random.randint(0, 100) < 1:
    #     print("Faster!")
    #     obstacle_speed *= 1.1
    #pygame.time.delay(1000//10+speedaddition)
    # clock.tick(60)
    obstacle_speed = math.log(max(5,int(score)),30)


    dt = clock.tick(60)/1000

pygame.quit()