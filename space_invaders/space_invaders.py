import pygame
import objects
# Improvements für objects:
# nur ein globales Field
# bullet, mob, player, base, rock colors machen

# TODO implement
def lose(score):
    print(score)


# aktuelles Problem: Bullets checken nur das komplette Rectangle
def collision(entity, bullet):
    if entity.x[0] <= bullet.x[0] and bullet.x[0] <= entity.x[1]:
        if bullet.y[1] >= entity.y[0]:
            entity.take_dmg(bullet.dmg)
            bullet.die()

def collision_rock_mob(rock, mob):
    if rock.x[0] <= mob.x[0] and mob.x[0] <= rock.x[1]:
        if mob.y[1] >= rock.y[0]:
            mob.die()
            rock.take_dmg(mob.max_hp)

# TODO - Implement draw function
# move funktion aller entities gleiche signatur machen
def draw(entity):
    pass

# TODO delte when useles:
def temp():
    """
    00000000000000000000000000000000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00011111001111100111110011111000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00000000000000000000000000000000
    00001111000001110000000001111100
    00001111000001110000000001111100
    00000000000000000000000000000000
    00000000000PPPPP0000000000000000
    BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    """
    pass

def next_wave(moblist: MobList):
    wave = moblist.wave
    mobA_list = []
    mobB_list = []
    mobC_list = []
    value_mobA =  int(10*(1.2**wave))
    value_mobB =  int(10*(1.2**(wave+1)))
    value_mobC =  int(10*(1.2**(wave+2)))
    attack_cooldown_mobA = max(3,5-0.1*wave)
    attack_cooldown_mobB = max(1,3-0.1*wave)
    attack_cooldown_mobC = max(2,4-0.1*wave)

    for i in range(4):
        x_cords = 3+i*7
        mobA = Mob(x_cords,1,4,2, 1, attack_cooldown_mobA, value_mobA, 2, 3, [161, 8, 8])
        mobA_list.append(mobA)

        mobB = Mob(x_cords,6,4,2, 1, attack_cooldown_mobB, value_mobB, 2, 2, [92, 29, 140])
        mobB_list.append(mobB)
        
        mobC = Mob(x_cords,11,4,2, 2, attack_cooldown_mobC, value_mobC, 2, 4, [40, 29, 140])
        mobC_list.append(mobC)

    moblist.add_row(mobA_list)
    moblist.add_row(mobB_list)
    moblist.add_row(mobC_list)
    moblist.reset_dead_columns()

    # if wave = 1:
    # # 1 Wave:
    #     mob1A = Mob(x,y,x+,y+, 1, 5, 10, 2, 3, [161, 8, 8])
    #     mob1B = Mob(x,y,x+,y+, 1, 3, 12, 2, 2, [92, 29, 140])
    #     mob1C = Mob(x,y,x+,y+, 1, 4, 14, 2, 4, [40, 29, 140])
    # if wave = 2:
    #     # 2 Wave:
    #     mob2A = Mob(x,y,x+,y+, 1, 4.9, 12, 2, 3, [161, 8, 8])
    #     mob2B = Mob(x,y,x+,y+, 1, 2.9, 14, 2, 2, [92, 29, 140])
    #     mob2C = Mob(x,y,x+,y+, 1, 3.9, 16, 2, 4, [40, 29, 140])
    # if wave = 3:
    # # 3 Wave:
    #     mob3A = Mob(x,y,x+,y+, 1, 4.8, 14, 2, 3, [161, 8, 8])
    #     mob3B = Mob(x,y,x+,y+, 1, 2.8, 16, 2, 2, [92, 29, 140])
    #     mob3C = Mob(x,y,x+,y+, 1, 3.8, 19, 2, 4, [40, 29, 140])

def reset_rocks(rock_list):
    
    rock_list[0] = Rock(4,24,3,2,8)
    rock_list[1] = Rock(13,24,2,2,6)
    rock_list[2] = Rock(25,24,4,2,10)


# Game
player = objects.Player(14,30,5,0,max_hp=3)
base = objects.Base(10)
score=0
running=True
mob_list = objects.MobList([])
bullet_list=[]
bullet_list.append(player.bullet)

rock_list=[]
pygame.init()
SCALE=12
# screen = pygame.display.set_mode((32*SCALE, 32*SCALE))
clock = pygame.time.Clock()
dt = 0





while running:

    # TODO
    # # Player Moves
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_a]:
    #     print("a")
    #     player.move(dt,1,-1)
    #     print(player.x)

    # if keys[pygame.K_d]:
    #     print("d")
    #     player.move(dt,1,1)
    #     print(player.x)
    
    # Mobs Move (only move forward atm)
    for mob in mob_list.get_all():
        mob.move(dt,0,-1)
    
    
    # Bullets Move
    for bullet in bullet_list:
        bullet.travel(dt)

    # Bullets are shot
    # Player Bullet is shot
    if keys[pygame.K_w]:
        player.shoot()

    bullet_list = []
    if player.bullet.is_alive():
        bullet_list.append(player.bullet)
    
    # Mob Bullets are shot
    for mob in mob_list.get_first_row():
        mob.shoot(dt)
        bullet_list.append(mob.bullet)

    # Bullet-Collisions
    for bullet in bullet_list:
        
        # Bullet Player Collision
        # If bullet isnt alive: skip the iteration
        if not bullet.is_alive():
            continue
        collision(player, bullet)

        # Bullet Base Collision
        if not bullet.is_alive():
            continue
        collision(base, bullet)
            
        # Bullet Rock Collisions
        if not bullet.is_alive():
            continue
        for rock in rock_list:
            if bullet.is_alive() and rock.is_alive():
                collision(rock,bullet)

        # Bullet Mob Collisions
        if not bullet.is_alive():
            continue
        for mob in mob_list.get_firt_row():
            if bullet.is_alive() and mob.is_alive():
                collision(mob, bullet)
                if not mob.is_alive():
                    score = score + mob.value
    
    # Mob Rock Collision
    for mob in mob_list.get_firt_row:
        if mob.is_alive():
            for rock in rock_list:
                if rock.is_alive():
                    collision_rock_mob(rock,mob)

    # adjust current mobs
    mob_list.update()

    # Check Lose Condition
    if (not player.is_alive()) or (not base.is_alive()):
        lose(score)


    # If all Mob objects are dead => new wave
    if mob_list.all_dead():
        reset_rocks(rock_list)
        next_wave(mob_list)
    
    # Draw all Objects:
    for entity in [player]+[base]+[mob_list]+[rock_list]:
        draw(entity)


    dt = clock.tick(60) / 1000
    print("dt: ", dt)


# b = objects.Bullet(15,5,0,0,5,2,1)
# print("Position: ",b.x,b.y)
# print("IsAlive?: ",b.is_alive())
# b.travel(20)
# print("Position: ",b.x,b.y)
# print("IsAlive?: ",b.is_alive())