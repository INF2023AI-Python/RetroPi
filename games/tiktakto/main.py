import pygame
import sys

pygame.init()

# defining the game field
scale = 25
screen_height = 32 * scale
screen_width = 32 * scale
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tic Tac Tobi')
color = (255, 0, 0)

# defining the moving rectangle
x = 11*scale  # start position
y = 1*scale
width = 10*scale  # size
height = 10*scale
vel = 10*scale  # velocity

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated

running = True  

player_circle = set([])
player_x = set([])


while running:

    #printing the game board
    screen.fill((0, 0, 0))   # Clear the screen and set the screen background
    

    


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 1*scale:  #movment of the blue box
        x -= vel
    if keys[pygame.K_RIGHT] and x < 21*scale:
        x += vel
    if keys[pygame.K_UP] and y > 1*scale:
        y -= vel
    if keys[pygame.K_DOWN] and y < 21*scale:
        y += vel

   


    if keys[pygame.K_a] and ((x,y) not in player_x) and len(player_circle) <= len(player_x):
        player_circle.add((x,y))
        
        
    if keys[pygame.K_c] and ((x,y) not in player_circle) and (len(player_circle) > len(player_x)):
        player_x.add((x,y))
       
        
        
        
    

    for i in player_circle:
        pygame.draw.circle(screen,(255, 255, 255),[i[0] + 5*scale, i[1] + 5*scale], 4*scale, 1*scale)
    
    for i in player_x:
        pygame.draw.line(screen, (255, 255, 255), [i[0] + 1*scale, i[1] + 1*scale], [i[0] + 9*scale, i[1] + 9*scale], 1*scale)
        pygame.draw.line(screen, (255, 255, 255), [i[0] + 1*scale , i[1] + 9*scale], [i[0] + 9*scale, i[1] + 1*scale], 1*scale)


    








    pygame.draw.rect(screen, color, [1*scale, 1*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [11*scale, 1*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [21*scale, 1*scale, 10*scale, 10*scale], 1*scale)

    pygame.draw.rect(screen, color, [1*scale, 11*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [11*scale, 11*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [21*scale, 11*scale, 10*scale, 10*scale], 1*scale)

    pygame.draw.rect(screen, color, [1*scale, 21*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [11*scale, 21*scale, 10*scale, 10*scale], 1*scale)
    pygame.draw.rect(screen, color, [21*scale, 21*scale, 10*scale, 10*scale], 1*scale)

    pygame.draw.rect(screen, (0, 0, 255), [x, y, width, height], 1*scale)

    pygame.display.flip()  # refreshes the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
            running = False  # ends pygamges

    clock.tick(15) 





#Spielllogik




# pygame.display.quit()

#draw hier und dort etwas 
#definier x und o 
#input ein feld higliten und 

#überprüfe auf win 