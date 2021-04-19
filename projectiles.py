import pygame
import sys
import math
from constants import *


class projectile():

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

    def projectiles_update(array):
        
        for bullets in array:
            bullets.projectile_move(self)
            bullets.projectile_draw(self, screen)

