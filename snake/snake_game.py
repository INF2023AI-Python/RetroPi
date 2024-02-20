import pygame
import random
import copy
import os

running = True

SCALE = 16
pygame.init()

"""
logic:
 spawnsnake
 spawnapple
    down spawn in snake
 movesnake
    head moves one step
    tail moves to the last head position

 checkforEvents/collision
 loop
"""
speed = 10
tail = []
clist = []

global snake_dir
snake_dir = (0, 1)


def spawn_snake():
    for i in range(1, 30):
        x = pygame.Rect(i * (SCALE + 1), 1 * (SCALE+1), 1 * SCALE, 1 * SCALE)
        tail.append(x)
        clist.append(x)


def spawn_apple():
    x = random.randint(0, SCALE)
    y = random.randint(0, SCALE)
    return pygame.draw.rect(screen, "yellow", (x * (SCALE + 1), y * (SCALE + 1), SCALE, SCALE))


def move_snake():
    # move n to n-1
    # for i in range(0,len(tail)-1):
    global snake_dir
    for i in range(0, len(tail) - 1):
        tail[i + 1] = copy.deepcopy(clist[i])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_dir = (0, -1)
    elif keys[pygame.K_a]:
        snake_dir = (-1, 0)
    elif keys[pygame.K_s]:
        snake_dir = (0, 1)
    elif keys[pygame.K_d]:
        snake_dir = (1, 0)
    SPEED = 17
    tail[0].move_ip(SPEED * snake_dir[0], SPEED * snake_dir[1])
    for i, e in enumerate(tail):
        clist[i] = copy.deepcopy(tail[i])


def check_events():
    pass


screen = pygame.display.set_mode((32 * SCALE, 32 * SCALE))
clock = pygame.time.Clock()
spawn_snake()
apple = spawn_apple()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    move_snake()
    check_events()
    head = tail[0]
    for i, e in enumerate(tail):
        if i == 0:
            continue
        else:
            pygame.draw.rect(screen, "green", e)
    pygame.draw.rect(screen, "red", head)
    pygame.draw.rect(screen, "red", apple)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(3) / 1000

pygame.quit()
