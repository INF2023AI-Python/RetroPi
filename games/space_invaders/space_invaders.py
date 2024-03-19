def start_spaceinvader(matrix, joystick_found, joystick, draw, image):
    import pygame
    from games.space_invaders import objects

    pygame.init()

    def lose(score):
        print(score)

    def overlap(x1, y1, x2, y2):
        # Check if either rectangle is entirely to the left or right of the other
        if max(x1) < min(x2) or max(x2) < min(x1):
            return False

        # Check if either rectangle is entirely above or below the other
        if max(y1) < min(y2) or max(y2) < min(y1):
            return False

        return True

    def collision(entity, bullet):
        if overlap(entity.x, entity.y, bullet.x, bullet.y):
            entity.take_dmg(bullet.dmg)
            bullet.die()

    def collision_rock_mob(rock, mob):
        if overlap(rock.x, rock.y, mob.x, mob.y):
            rock.take_dmg(mob.max_hp * 3)
            mob.die()

    def draw_entity(entity):
        draw.rectangle([entity.x[0], entity.y[0], entity.x[1], entity.y[1]],
                       fill=(entity.color[0], entity.color[1], entity.color[2]))

    def next_wave(moblist):
        MOB_SPEED = 1
        wave = moblist.wave
        mobA_list = []
        mobB_list = []
        mobC_list = []
        value_mobA = int(10 * (1.2 ** wave))
        value_mobB = int(10 * (1.2 ** (wave + 1)))
        value_mobC = int(10 * (1.2 ** (wave + 2)))
        attack_cooldown_mobA = max(3, 5 - 0.1 * wave)
        attack_cooldown_mobB = max(1, 3 - 0.1 * wave)
        attack_cooldown_mobC = max(2, 4 - 0.1 * wave)

        for i in range(4):
            x_cords = 3 + i * 7
            # mobA = first Row
            mobA = objects.Mob(x_cords, 11, 4, 2, 1, attack_cooldown_mobA, value_mobA, MOB_SPEED, [161, 8, 8])
            # mobA = objects.Mob(x_cords,1,4,2, 1, attack_cooldown_mobA, value_mobA, MOB_SPEED, [161, 8, 8])
            mobA_list.append(mobA)

            # mobB = second Row
            mobB = objects.Mob(x_cords, 6, 4, 2, 1, attack_cooldown_mobB, value_mobB, MOB_SPEED, [92, 29, 140])
            mobB_list.append(mobB)

            # mobC = third Row
            mobC = objects.Mob(x_cords, 1, 4, 2, 2, attack_cooldown_mobC, value_mobC, MOB_SPEED, [40, 29, 140])
            # mobC = objects.Mob(x_cords,11,4,2, 2, attack_cooldown_mobC, value_mobC, MOB_SPEED, [40, 29, 140])
            mobC_list.append(mobC)

        moblist.add_row(mobA_list)
        moblist.add_row(mobB_list)
        moblist.add_row(mobC_list)
        moblist.wave = wave + 1

    def reset_rocks(rock_list):
        rock_list.append(objects.Rock(4, 24, 3, 2, 8))
        rock_list.append(objects.Rock(13, 24, 2, 2, 6))
        rock_list.append(objects.Rock(25, 24, 4, 2, 10))

    # Game Setup
    player = objects.Player(14, 30, 4, 0, max_hp=3, speed=8)
    base = objects.Base(10)
    score = 0
    running = True
    mob_list = objects.MobList()
    next_wave(mob_list)

    bullet_list = []
    bullet_list.append(player.bullet)

    rock_list = []
    reset_rocks(rock_list)
    SCALE = 12
    # screen = pygame.display.set_mode((32*SCALE, 32*SCALE))
    clock = pygame.time.Clock()
    dt = 0

    while running:
        # Resetting Image
        draw.rectangle([0, 0, 32, 32], fill=(0, 0, 0))
        # Check for Quitting
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

        x_axis = 0
        shoot_button = False
        if joystick_found:
            if joystick.get_button(10):
                running = False
            x_axis = joystick.get_axis(0)
            shoot_button = joystick.get_button(11)

        x_axis = 0 if abs(x_axis) < 0.1 else x_axis
        # Player Moves
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or x_axis > 0:
            player.move(dt, -1)

        if keys[pygame.K_d] or x_axis < 0:
            player.move(dt, 1)

        # Mobs Move
        for mob in mob_list.get_all():
            mob.move(dt, 0, 1)

        # Bullets Move
        for bullet in bullet_list:
            bullet.travel(dt)

        # Bullets are shot
        # Player Bullet is shot
        if keys[pygame.K_w] or shoot_button:
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
                    collision(rock, bullet)

            # Bullet Mob Collisions
            if not bullet.is_alive():
                continue
            for mob in mob_list.get_first_row():
                if bullet.is_alive() and mob.is_alive():
                    collision(mob, bullet)
                    if not mob.is_alive():
                        score = score + mob.value

        # Bullet-Bullet Collision
        # Bullet-Bullet somtimes fails when the collision happens close to the player - the player bullet dies
        if player.bullet.is_alive():
            if len(bullet_list) > 1:
                main_bullet = bullet_list[0]
                for bullet in bullet_list[1:]:
                    if overlap(main_bullet.x, main_bullet.y, bullet.x, bullet.y):
                        main_bullet.die()
                        bullet.die()
                        break

        # Mob-Rock / Mob-Base / Mob-Plyer Collision
        for mob in mob_list.get_first_row():
            if mob.is_alive():
                for rock in rock_list + [base] + [player]:
                    if rock.is_alive():
                        collision_rock_mob(rock, mob)

        # Adjust current mobs
        mob_list.update()

        # Check Lose Condition
        if (not player.is_alive()) or (not base.is_alive()):
            lose(score)
            break

        # Next Wave
        if mob_list.get_first_row() == []:
            reset_rocks(rock_list)
            next_wave(mob_list)

        # Preparing mobs for drawing
        mobs = mob_list.get_all()
        if mobs == [[], [], [], []]:
            mobs = []

        # Draw all Objects:
        for entity in [player] + [base] + rock_list + mobs + bullet_list:
            if entity.is_alive():
                draw_entity(entity)

        # Update Matrix-Image
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60) / 1000
