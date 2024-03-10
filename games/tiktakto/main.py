import pygame
import sys

pygame.init() 

#defining the game field 
scale = 10
screen_height = 32*scale
screen_width = 32*scale
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tic Tac Tobi')

color=(255, 0, 0)


#Hält spiel offen 
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

  
    pygame.display.flip()  # Aktualisiere den Bildschirm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # wenn spieler Fenster schließt -> Schleife wird beendet 
            running = False             # Beenden von Pygame



#Spielllogik




# pygame.display.quit()

#draw hier und dort etwas 
#definier x und o 
#input ein feld higliten und 

#überprüfe auf win 