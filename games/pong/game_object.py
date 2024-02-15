import pygame

class GameObject:

    def __init__(self, rect:pygame.Rect, speed:pygame.Vector2):
        self.rect = rect
        self.speed = speed        
        self.x = rect.left
        self.y = rect.top

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def set_speed(self, speed_x, speed_y):
        self.speed.x = speed_x
        self.speed.y = speed_y

    def update(self,deltaTime):
        self.set_position(self.x+ (self.speed.x * deltaTime), self.y + (self.speed.y * deltaTime))