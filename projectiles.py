import pygame
import sys
import math
from constants import *


class Projectile():

    def __init__(self, x_position, y_position, speed, color, radius, direction):

        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.color = color
        self.radius = radius 
        self.direction = direction

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):

        self.x += self.direction[0] * self.speed  
        self.y += self.direction[1] * self.speed

    def is_out_of_bound(self):

        if self.x<0 or self.x>WIDTH or self.y<0 or self.y>HEIGHT:
            return True
        else:
            return False


class Sprites():


    def __init__(self):

        self.projectiles = []
        self.enemeies = []

    def add_projectile(self, x_position, y_position, direction):

        self.projectiles.append(Projectile(x_position, y_position, PROJECTILE_SPEED, YELLOW, PROJECTILE_RADIUS, direction))

    def update(self):

        print(self.projectiles)

        for projectile in self.projectiles:

            projectile.move()
            if projectile.is_out_of_bound():
                self.projectiles.remove(projectile)
                del projectile

    def draw(self, screen):

        for projectile in self.projectiles:

            projectile.draw(screen)



