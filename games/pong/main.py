import pygame

pygame.init()

SCALE = 20

screen = pygame.display.set_mode((40*SCALE, 40*SCALE))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 10, screen.get_height() / 2)
ball_pos = 0
PLAYER_SPEED = 400
BALL_SPEED = 600

playing_field = pygame.Rect(0,0,32*SCALE,32*SCALE)


def withinBoard(rect:pygame.Rect):
    return playing_field.contains(rect)

size= 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player_box = pygame.Rect(0,player_pos.y,1*SCALE,6*SCALE+size)
    #ball_box = pygame.Rect(ball_pos.x,ball_pos.y,ball_pos.xx,ball_pos.yy)

    #draw gameobjects
    pygame.draw.rect(screen, "green", playing_field)
    pygame.draw.rect(screen, "white", player_box)
    #pygame.draw.rect(screen, "white", ball_box)

    #update variable for gameobjects
    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and withinBoard(player_box):
        if (player_pos.y - PLAYER_SPEED * dt) < 0:
            player_pos.y = 0
        else:
            player_pos.y -= PLAYER_SPEED * dt
    if keys[pygame.K_s] and withinBoard(player_box):
        if ((player_pos.y+player_box.height) + PLAYER_SPEED * dt) > (32*SCALE):
            player_pos.y = 32*SCALE-player_box.height
        else:
            player_pos.y += PLAYER_SPEED * dt

    #ball movement
    
    #if ball collision  
    #if     player collide x flip
    #if    top or bottom y flip
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    



pygame.quit()