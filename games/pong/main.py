import pygame

# pygame setup
pygame.init()


SCALE = 20
screen = pygame.display.set_mode((32*SCALE, 32*SCALE))


clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 10, screen.get_height() / 2)
SPEED = 300


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    box = pygame.Rect(player_pos.x,player_pos.y,1*SCALE,6*SCALE)
    pygame.draw.rect(screen, "white", box)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]     :
        player_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()