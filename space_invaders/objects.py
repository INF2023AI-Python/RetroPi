# Game Object Classes

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

    def __init__(self, x_pos, y_pos, x_size, y_size, max_hp, size, attack_speed, value, speed):
        super().__init__(x_pos, y_pos, x_size, y_size)
        
        self.max_hp = max_hp
        self.hp = max_hp
        
        self.size = size
        self.attack_speed = attack_speed
        self.value = value
        self.speed = speed

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp <= 0:
            self.die()
    

    def move(self, time, x_dir, y_dir):
        self.set_x_pos(x_dir*time*self.speed)
        self.set_y_pos(y_dir*time*self.speed)

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
        self.bullet = Bullet(0,0,0,0,0,0,0)
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
        elif self[0] < 0:
            self.x[0] = 0
            self.x[1] = self.x_size

    def shoot(self):
        if not self.bullet.is_alive():
            # TODO Bullet spawn place
            self.bullet = Bullet(self.x[0], self.y[0], self.x_size, self.y_size, dmg = 1, speed = 2, direction = -1)
            #return self.bullet 

class Rock(Entity):

    def __init__(self, x_pos, y_pos, x_size, y_size, max_hp):
        super().__init__(x_pos, y_pos, x_size, y_size)
        self.max_hp = max_hp
        self.hp = max_hp
        self.color=[0,255,0]

    # TODO: add color
    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
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