# Game Object Classes
import random

class Field:
    def __init__(self,x_size,y_size):
        self.x_size = x_size
        self.y_size = y_size

class Entity:

    def __init__(self, x_pos, y_pos, x_size, y_size):
        self.x = [x_pos,x_pos+x_size]
        self.x_size = x_size
        self.y = [y_pos,y_pos+y_size]
        self.y_size = y_size

        self.alive = True

        self.field = Field(31,31)

    def set_x_pos(self, x_pos):
        self.x = [x_pos,x_pos+self.x_size]

    def set_y_pos(self, y_pos):
        self.y = [y_pos,y_pos+self.y_size]

    def is_alive(self):
        return self.alive

    def set_alive(self, status):
        self.alive = status

    def die(self):
        self.alive = False

class Mob(Entity):

    def __init__(self, x_pos, y_pos, x_size, y_size, max_hp, attack_cooldown, value, speed, cooldown, color):
        super().__init__(x_pos, y_pos, x_size, y_size)
        
        self.max_hp = max_hp
        self.hp = max_hp
        
        self.attack_cooldown = attack_cooldown
        self.cooldown = cooldown
        self.value = value
        self.speed = speed

        self.bullet = Bullet(-1,-1,0,0,0,0,0)
        self.bullet.die()

        self.color=color

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp <= 0:
            self.die()
    
    def move(self, time, x_dir, y_dir):
        self.set_x_pos(self.x[0]+x_dir*time*self.speed)
        self.set_y_pos(self.y[0]+y_dir*time*self.speed)

    def shoot(self,time):
        self.cooldown = self.cooldown + time
        if self.cooldown > self.attack_cooldown:
            if not self.bullet.is_alive():
                self.cooldown = 0
                if random.randint(1,9) <= 2:
                    x_place = (self.x[0] + self.x[1])/2
                    self.bullet = Bullet(x_place, self.y[1]+1, 0, 1, dmg = 1, speed = 2, direction = 1)
            

class Bullet(Entity):

    def __init__(self, x_pos, y_pos, x_size, y_size, dmg, speed, direction):
        super().__init__(x_pos, y_pos, x_size, y_size)
        self.dmg = dmg
        self.speed = speed 
        self.direction = direction
        self.color = [100, 100, 100]

    def travel(self, time):
        self.y[0] = self.y[0]+self.speed*self.direction*time
        self.y[1] = self.y[1]+self.speed*self.direction*time
        if self.y[0] > self.field.y_size or self.y[1] < 0:
            self.die()
   
class Player(Entity):

    def __init__(self, x_pos, y_pos, x_size, y_size, max_hp):
        super().__init__(x_pos, y_pos, x_size, y_size)
        self.max_hp = max_hp
        self.hp = max_hp
        self.color = [0,255,0]
        self.shooting = False
        self.bullet = Bullet(-1,-1,0,0,0,0,0)
        self.bullet.die()

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg

        self.color[1] = max(0,int(self.color[1] * (self.hp/self.max_hp)))
        self.color[0] = (255-color[1])
        
        if self.hp <= 0:
            self.die()

        
    def move(self, time, speed, direction):
        change = time*speed*direction
        self.x[0] = self.x[0]+change
        self.x[1] = self.x[1]+change
        
        if self.x[1] > self.field.x_size:
            self.x[1] = self.field.x_size
            self.x[0] = self.x[1] - self.x_size
        elif self.x[0] < 0:
            self.x[0] = 0
            self.x[1] = self.x_size

    def shoot(self):
        if not self.bullet.is_alive():
            x_place = (self.x[0] + self.x[1])/2
            self.bullet = Bullet(x_place, self.y[0]-2, 0, 1, dmg = 1, speed = 2, direction = -1)
            

class Rock(Entity):

    def __init__(self, x_pos, y_pos, x_size, y_size, max_hp):
        super().__init__(x_pos, y_pos, x_size, y_size)
        self.max_hp = max_hp
        self.hp = max_hp
        self.color=[105,105,105]

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        self.color = [105*(self.hp/self.max_hp)]*3
        if self.hp <= 0:
            self.die()



class Base(Entity):
    def __init__(self, max_hp):
        super().__init__(x_pos=0, y_pos=31, x_size=31, y_size=0)
        self.max_hp = max_hp
        self.hp = max_hp

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg

        self.color[1] = max(0,int(self.color[1] * (self.hp/self.max_hp)))
        self.color[0] = (255-color[1])
        
        if self.hp <= 0:
            self.die()


class MobList:
    # list_of_list_of_mobs [[col1_mobs],[col2_mobs],...]
    def __init__(self):
        self.list = [[],[],[],[]]
        self.dead_columns = [False, False, False, False]
        self.wave = 0

    def add_row(self, row_of_mobs):
        if len(row_of_mobs) != len(self.list):
            print("Amount of Mobs in Row doesn't match the amount of columns.")
            return

        for columns, row_elements zip(self.list, row_of_mobs):
            columns.append(row_elemnts)
        
    def update(self):
        len_list = len(self.list)-1
        if len_list < 0:
            print("List of Mobs is to short.")
            return

        # for each mob: if a mob is behind the mob, it is deleted and the mob behind is pushed
        # ahead,allowing it to shoot.
        for i in range(len_list):
            if not self.list[i][0].is_alive():
                if len(self.list[i]) > 0:
                    del self.list[i][0]
                
                # to save, if all mobs of a columns are dead
                else:
                    self.dead_columns[i] = True

    def get_first_row(self):
        result = []
        for columns in self.list:
            result.append(columns[0])
        return result
    
    def get_all(self):
        singular_list = [item for sublist in self.list for item in sublist]
        return singular_list
    
    def all_dead():
        a = True
        for col_status in self.dead_columns:
            a = a and col_status
        return a
    
    def reset_dead_columns(self):
        self.dead_columns = [False, False, False, False]
        
# useless da nicht jeder move 1 pixel ist
# class MobMove:

#     def __init__(self,steps):
#         self.step = -1
#         self.len_steps = len(steps)
#         self.steps = steps
    
#     def take_step(self):
#         self.step = ((self.step+1) % self.len_steps)
#         return self.steps[self.step]
