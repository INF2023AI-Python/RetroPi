import pygame
import sys

pygame.init()

#defining the game field 
running = True
scale = 10
screen_height = 32*scale
screen_width = 32*scale
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Tic Tac Tobi')


#Hält spiel offen 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # wenn spieler Fenster schließt -> Schleife wird beendet 
            running = False




# Beenden von Pygame





# pygame.display.quit()

#draw hier und dort etwas 
#definier x und o 
#input ein feld higliten und 

#überprüfe auf win 