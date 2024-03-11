import objects    
# Improvements für objects:
# nur ein globales Field
# bullet, mob, player, base, rock colors machen

"""
Idee für gameloop und drawen von einzelnen objekten:
    for object in list_objects:
        if object.is_alive():
            draw(object)
"""

# TODO implement
def game_loss(score):
    print(score)

# TODO: implement next_wave
def next_wave(mob_list):
    pass

# TODO - aktuelles Problem: Bullets checken nur das komplette Rectangle
def collision(entity, bullet):
    if entity.x[0] <= bullet.x[0] and bullet.x[0] <= entity.x[1]:
        if bullet.y[1] >= entity.y[0]:
            entity.take_dmg(bullet.dmg)
            bullet.die()

# TODO - Implement draw function
# move funktion aller entities gleiche signatur machen
def draw(entity):
    pass

# Game
player = objects.Player(14,30,5,0,max_hp=3)
base = objects.Base(10)
score=0
running=True
mob_list=[]
bullet_list=[]
rock_list=[]

while running:

    # Player Moves
    # Mobs Move
    # Bullets Move

    # Bullet-Collisions
    for bullet in bullet_list:
        # Bullet Player Collision
        if bullet.is_alive():
            collision(player, bullet)

        # Bullet Base Collision
        if bullet.is_alive():
            collision(base, bullet)

        # Bullet Rock Collisions
        for rock in rock_list:
            if bullet.is_alive():
                collision(rock,bullet)

        # Bullet Mob Collisions
        for mob in mob_list:
            if bullet.is_alive():
                collision(mob, bullet)
        
    # Check Lose Condition
    if (not player.is_alive()) or (not base.is_alive()):
        print("B")
    # Debug:
    a = input("Waiting")

    # If all Mob objects are dead => new wave
    all_mob_status = [x.is_alive() for x in mob_list]

    if True not in all_mob_status:
        next_wave(mob_list)
    
    # Draw all Objects:
    for entity in [player]+[base]+[mob_list]+[rock_list]:
        draw(entity)


a = input("Exit?")