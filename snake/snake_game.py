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
head = pygame.Rect(0,1*SCALE,1*SCALE,1*SCALE)
tail = []

def spawn_snake():
    for i in range(1,5):
        x = pygame.Rect(i*(SCALE+1),1*SCALE,1*SCALE,1*SCALE)
        tail.append(x)

def spawn_apple():
    pass

def move_snake():
    temp = tail[0]
    tail[0] = copy.deepcopy(head)
    #head = tail[0]
    temp2 = tail[1]
    tail[1] = temp
    tail[2] = temp2
    head.move_ip(0,16)
    print(head)

    #first element to head
    #1 - 0
    #2 - 1


def check_events():
    pass

screen = pygame.display.set_mode((32*SCALE, 32*SCALE))
clock = pygame.time.Clock()
spawn_snake()
spawn_apple()
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
    pygame.draw.rect(screen,"red",head)
    for e in tail:
        pygame.draw.rect(screen,"green",e)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(2) / 1000


pygame.quit()