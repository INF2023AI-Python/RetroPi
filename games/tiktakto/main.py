import pygame
import sys

pygame.init()

# defining the game field and general settings
scale = 10
screen_height = 32 * scale
screen_width = 32 * scale
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tic Tac Tobi')
color = (255, 0, 0)
font = pygame.font.SysFont(None, 40)

# defining the moving rectangle
x = 11*scale  # start position
y = 1*scale
width = 10*scale  # size
height = 10*scale
vel = 10*scale  # velocity

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
running = True
game_over = False
player= 0

#Tuple to write positions x and y
player_circle = set([])
player_x = set([])

while running:
    screen.fill((0, 0, 0))   # Clear the screen and set the screen background

    #movment of the blue box
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 1*scale:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 21*scale:
        x += vel
    if keys[pygame.K_UP] and y > 1*scale:
        y -= vel
    if keys[pygame.K_DOWN] and y < 21*scale:
        y += vel

    #condition to draw a cirlce or an x
    if keys[pygame.K_a] and ((x,y) not in player_x) and len(player_circle) <= len(player_x) and game_over == False and player == 0:
        player_circle.add((x,y))
        player = 1
    if keys[pygame.K_a] and ((x,y) not in player_circle) and (len(player_circle) > len(player_x)) and game_over == False and player == 1:
        player_x.add((x,y))
        player = 0

    #draws x or circle
    for i in player_circle:
        pygame.draw.circle(screen,(255, 255, 255),[i[0] + 5*scale, i[1] + 5*scale], 4*scale, 1*scale)
    for i in player_x:
        pygame.draw.line(screen, (255, 255, 255), [i[0] + 1*scale, i[1] + 1*scale], [i[0] + 9*scale, i[1] + 9*scale], 1*scale)
        pygame.draw.line(screen, (255, 255, 255), [i[0] + 1*scale , i[1] + 9*scale], [i[0] + 9*scale, i[1] + 1*scale], 1*scale)

    #printing the game board
    for o in range(1, 22, 10):
        for i in range(1, 22, 10):
            pygame.draw.rect(screen, color, [i*scale, o*scale, 10*scale, 10*scale], 1*scale)

    #moving rectangle to trac position
    pygame.draw.rect(screen, (0, 0, 255), [x, y, width, height], 1*scale)

    #check for win for player_circle
    #Horizontal
    if (1*scale,1*scale) in player_circle and (11*scale,1*scale) in player_circle and (21*scale,1*scale) in player_circle : #wenn winner == true muss player_circle wins stehen und play again button
        winner = 0
        game_over = True
    if (1*scale,11*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,11*scale) in player_circle :
        winner = 0
        game_over = True
    if (1*scale,21*scale) in player_circle and (11*scale,21*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    #Vertical
    if (1*scale,1*scale) in player_circle and (1*scale,11*scale) in player_circle and (1*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (11*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (11*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (21*scale,1*scale) in player_circle and (21*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    #Diogonal
    if (1*scale,1*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,21*scale) in player_circle :
        winner = 0
        game_over = True
    if (1*scale,21*scale) in player_circle and (11*scale,11*scale) in player_circle and (21*scale,1*scale) in player_circle :
        winner = 0
        game_over = True

    #check for win for player_x
    #Horizontal
    if (1*scale,1*scale) in player_x and (11*scale,1*scale) in player_x and (21*scale,1*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,11*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,11*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,21*scale) in player_x and (11*scale,21*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    #Vertical
    if (1*scale,1*scale) in player_x and (1*scale,11*scale) in player_x and (1*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (11*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (11*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (21*scale,1*scale) in player_x and (21*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    #Diogonal
    if (1*scale,1*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,21*scale) in player_x :
        winner = 1
        game_over = True
    if (1*scale,21*scale) in player_x and (11*scale,11*scale) in player_x and (21*scale,1*scale) in player_x :
        winner = 1
        game_over = True

    #checks for tie
    if len(player_circle) == 5 and len(player_x) == 4:
        winner = 2
        game_over = True
    if len(player_circle) == 4 and len(player_x) == 5:
        winner = 2
        game_over = True

    #End_test who has won
    if game_over == True and winner == 0:
        #ruft o wins auf
        pass
    if game_over == True and winner == 1:
         #ruft x wins auf
        pass
    if game_over == True and winner == 2:
         #ruft tie auf. tie fehlt auf matrix ?
        pass

    print(player_circle)


    pygame.display.flip()  # refreshes the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player is closing the window -> the loop will be closed
            running = False  # ends pygamges
    clock.tick(15)

