import pygame
import sys

pygame.init()

# defining the game field
scale = 10
screen_height = 32 * scale
screen_width = 32 * scale
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tic Tac Tobi')
color = (255, 0, 0)

# defining the moving rectangle
x = 110  # start position
y = 10
width = 100  # size
height = 100
vel = 100  # velocity

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated

running = True  
while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, [10, 10, 100, 100], 10)
    pygame.draw.rect(screen, color, [110, 10, 100, 100], 10)
    pygame.draw.rect(screen, color, [210, 10, 100, 100], 10)

    pygame.draw.rect(screen, color, [10, 110, 100, 100], 10)
    pygame.draw.rect(screen, color, [110, 110, 100, 100], 10)
    pygame.draw.rect(screen, color, [210, 110, 100, 100], 10)

    pygame.draw.rect(screen, color, [10, 210, 100, 100], 10)
    pygame.draw.rect(screen, color, [110, 210, 100, 100], 10)
    pygame.draw.rect(screen, color, [210, 210, 100, 100], 10)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 10:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 210:
        x += vel
    if keys[pygame.K_UP] and y > 10:
        y -= vel
    if keys[pygame.K_DOWN] and y < 210:
        y += vel

    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))

    pygame.display.flip()  # refreshes the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
            running = False  # ends pygamges

    clock.tick(6) 





#Spielllogik




# pygame.display.quit()

#draw hier und dort etwas 
#definier x und o 
#input ein feld higliten und 

#überprüfe auf win 