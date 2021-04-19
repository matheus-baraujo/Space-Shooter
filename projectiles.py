import pygame
import sys
import math
from constants import *


class Projectile():

    def __init__(self, position, speed, color, radius, direction):

        self.position = position
        self.speed = speed
        self.color = color
        self.radius = radius 
        self.direction = direction

    def projectile_draw(self, screen):

        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def projectile_move(self):

        self.position[0] += self.direction[0]*self.speed  
        self.position[1] += self.direction[1]*self.speed

    def update(self, screen):
        
        self.projectile_move()
        self.projectile_draw(screen)


class Sprites():


    def __init__(self):

        self.projectiles = []
        self.enemeies = []

    def add_projectile(self, position, direction):

        self.projectiles.append(Projectile(position, PROJECTILE_SPEED, YELLOW, PROJECTILE_RADIUS, direction))

    def update(self, screen):

        for projectile in self.projectiles:
            projectile.update(screen)

