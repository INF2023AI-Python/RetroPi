import pygame
import random
import math

def start_runner(matrix, joystick_found, joystick, draw, image):

    pygame.init()
    clock = pygame.time.Clock()

    def distance(obstacle,player):
        x_distance = obstacle[0]-player[0]
        y_distance = obstacle[1]-player[1]
        distance = math.sqrt(x_distance*x_distance + y_distance*y_distance)
        return distance

    def draw_top_bot():
        # ceiling
        draw.rectangle([0,0,32,7], fill = (80,80,80))
        # floor
        draw.rectangle([0,24,32,32], fill = (80,80,80))

    def draw_obstacle_list(obstacle_list):
        for obstacle in obstacle_list:
            draw.point([obstacle[0],obstacle[1]], fill = (255,0,0))

    def spawn_obstacle():
        return [31 ,random.randint(8,22)]

    def spawn_obstacle_y(y):
        return [31 ,y]

    def draw_player(player):
        draw.point([player[0],player[1]], fill = (255,255,255))

    def joystick_dir(joystick):
        threshold = 0.1
        y_axis = joystick.get_axis(1)

        if y_axis > threshhold:
            return 1
        if y_axis < -threshold:
            return -1

        return 0


    # Game statuses
    spawn_time_delay = 0.85
    spawn_timer = 0
    player = [3,23]
    player_dir = 1
    player_speed = 25
    obstacle_list = []
    obstacle_speed = 20
    score = 0
    increse_speed_timer = 0
    time_to_speed_increse = 8.5
    jump_lock = 0.125
    dt = 0
    running = True


    while running:
        # Resetting Image
        draw.rectangle([0,0,32,32],fill=(0,0,0))
        # Check for Quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        

        jump_lock = jump_lock - dt
        
        if jump_lock <= 0:
            if (keys[pygame.K_SPACE]):
                jump_lock = 0.125
                player_dir = -player_dir
            
            if joystick_found:
                if joystick.get_button(10):
                    running = False
                if joystick.get_button(11):
                    player_dir = -player_dir
                    jump_lock = 0.125
                if joystick_dir != 0:
                    player_dir = joystick_dir
                

        # player movement
        next_y = player[1] + player_dir*dt*player_speed

        player[1] = min(23,max(8,next_y))

        # obstacle movement
        obstacle_list = [(x-obstacle_speed*dt, y) for x, y in obstacle_list if x > 0]

        # collision detection 
        for obstacle in obstacle_list:
            # Lose Condition
            if distance(obstacle,player) < 1:
                running = False
                return {"game": "endlessrunner", "score":int(score)}

        # spawn new obstacle
        if spawn_timer >= spawn_time_delay:
            spawn_timer = 0
            if player[1] >= 22 and random.randint(1,4) <=3:
                obstacle_list.append(spawn_obstacle_y(23))

            elif player[1] <= 9 and random.randint(1,4) <=3:
                obstacle_list.append(spawn_obstacle_y(8))
            else:
                obstacle_list.append(spawn_obstacle())

        spawn_timer = spawn_timer+dt
        
        if increse_speed_timer >= time_to_speed_increse:
            increse_speed_timer = 0
            obstacle_speed = obstacle_speed*1.05
        
        increse_speed_timer = increse_speed_timer+dt

        # drawing
        draw_top_bot()
        draw_player(player)
        draw_obstacle_list(obstacle_list)

        score = score+dt
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(120)/1000
    return {"game":"runner", "score":score}