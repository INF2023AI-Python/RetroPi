import pygame


class GameObject:

    def __init__(self, rect:pygame.Rect, speed:pygame.Vector2):
        self.rect = rect
        self.speed = speed        
        self.x = rect.left
        self.y = rect.top

    # def get_rect(self):
    #     return self.rect
    
    # def get_speed(self):
    #     return self.speed

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def set_speed(self, speed_x, speed_y):
        self.speed.x = speed_x
        self.speed.y = speed_y

    def update(self,deltaTime):
        self.set_position(self.x+ (self.speed.x * deltaTime), self.y + (self.speed.y * deltaTime))


pygame.init()
SCALE = 20

screen = pygame.display.set_mode((40*SCALE, 40*SCALE))
clock = pygame.time.Clock()
running = True
dt = 0

PLAYER_SPEED = 20*SCALE
BALL_SPEED = 30*SCALE

player = GameObject(pygame.Rect(0,screen.get_height()/2,1*SCALE,6*SCALE),pygame.Vector2(0,PLAYER_SPEED))

#player_pos = pygame.Vector2(screen.get_width() / 10, screen.get_height() / 2) #comment due to player object


ball_pos = pygame.Vector2((screen.get_width()/2), (screen.get_height()/2))
playing_field = pygame.Rect(0,0,32*SCALE,32*SCALE)

next_tick_ball = pygame.Vector2(0,0)

def withinBoard(rect:pygame.Rect):
    return playing_field.contains(rect)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    wall = pygame.Rect(32*SCALE, 0, 1*SCALE, 32*SCALE)
    ball_box = pygame.Rect(ball_pos.x,ball_pos.y,10,10)
    #player_box = pygame.Rect(0,player_pos.y,1*SCALE,6*SCALE+size) #comment due to player object

    #draw gameobjects
    pygame.draw.rect(screen, "purple", wall)
    pygame.draw.rect(screen, "green", playing_field)
    pygame.draw.rect(screen, "white", player.rect)
    pygame.draw.rect(screen, "red", ball_box)

    #update variable for gameobjects
    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and withinBoard(player.rect):
        if (player.rect.top - (player.speed.y * dt)) < 0:
            player.rect.top = 0
        else:
            player.rect.top -= player.speed.y * dt

    if keys[pygame.K_s] and withinBoard(player.rect):
        if (player.rect.bottom + (player.speed.y * dt)) > (32*SCALE):
            player.rect.top=32*SCALE-player.rect.height
        else:
            player.rect.top += player.speed.y* dt


    
    #ball_box.
    #ball movement
    
    # next_tick_ball.x = ball_pos.x + BALL_SPEED * dt
    # next_tick_ball.y = ball_pos.y + BALL_SPEED * dt
    
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