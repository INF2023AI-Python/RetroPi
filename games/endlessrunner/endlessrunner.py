import pygame
import random

pygame.init()

WIDHT = 32
HEIGHT = 32
SCALE = 20

player_x = 5*SCALE
player_y = 28*SCALE
y_change = 0*SCALE
gravity = 1

screen = pygame.display.set_mode((WIDHT*SCALE, HEIGHT*SCALE))

timer = pygame.time.Clock()

running = True
while running:
    timer.tick(60)
    screen.fill((0, 0, 0))
    floor = pygame.draw.rect(screen, (255,255,255), (0, (HEIGHT-3)*SCALE, WIDHT*SCALE, 3*SCALE))
    player = pygame.draw.rect(screen, (255,0,0), (player_x, player_y, 1*SCALE, 1*SCALE))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
        if event.type == pygame.QUIT:
            running = False

    if y_change > 0 or player_y <  27*SCALE:
        player_y -= y_change
        y_change -= gravity
    if player_y < 28*SCALE:
        player_y = 28*SCALE
    if player_y == 28*SCALE and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()