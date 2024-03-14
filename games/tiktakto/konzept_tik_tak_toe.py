import pygame
import sys

pygame.init()

# Definiere die Fenstergröße und Farben
screen_width = 800
screen_height = 600
background_color = (0, 0, 0)
player_color = (0, 0, 255)

# Definiere die Geschwindigkeit der Bewegung
vel = 5

# Startposition der Figur
x = 50
y = 50
width = 50
height = 50

# Variablen zur Verfolgung der Bewegung in verschiedene Richtungen
move_left = False
move_right = False
move_up = False
move_down = False

# Variablen zur Verfolgung, ob die Bewegung schon ausgeführt wurde
last_move_left = False
last_move_right = False
last_move_up = False
last_move_down = False

# Erstelle das Fenster
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bewegende Figur")

running = True
while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not last_move_left:
                move_left = True
                last_move_left = True
            elif event.key == pygame.K_RIGHT and not last_move_right:
                move_right = True
                last_move_right = True
            elif event.key == pygame.K_UP and not last_move_up:
                move_up = True
                last_move_up = True
            elif event.key == pygame.K_DOWN and not last_move_down:
                move_down = True
                last_move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
                last_move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
                last_move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
                last_move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
                last_move_down = False

    if move_left:
        x -= vel
    if move_right:
        x += vel
    if move_up:
        y -= vel
    if move_down:
        y += vel

    pygame.draw.rect(screen, player_color, (x, y, width, height))
    pygame.display.flip()

pygame.quit()
sys.exit()
