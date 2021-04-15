import pygame
import sys
import math
from constants import *


class Spacecraft():


    '''
    This class will serve as a parent class for both Player class and Enemy class.
    Its purpose is to deal with basic movement that both the Player spacecraft and Enemy spacecraft will
    have to display.
    '''

    def __init__(self, x_position, y_position, life, speed, shape_function, color, angle_speed, angle):

        '''
        The x_position and y_position will be the coordenates of the center of the spacecraft.
        It will rotate around this point and translation will be calculated with it.

        life will keep track of many more hits the spacecraft can take before being destroyed

        speed will be a coeficient that will determine how many pixels per frame a spacecraft will move.

        shape_function will be a function that will determine the shape of the spacecraft. This will allow
        for more variety.

        color will be a RGB tuple that will determine color. The colors used should be in constants.py.

        angle will determine the original angle of the spacecraft with the y-axis, when it's created.

        angle_speed will work as speed for the angle.
        '''
        
        self.x, self.y = x_position, y_position
        self.vertices = shape_function(self.x, self.y)
        self.life = life
        self.speed = speed
        self.angle = angle
        self.angle_speed = angle_speed
        self.rotate_spacecraft(self.angle)

    def is_dead(self):

        '''
        This methods checks if a spacecraft life has reached zero.
        '''

        if self.life < 1:
            return False
        else:
            return True

    def register_hit(self, hitpoints=1):

        '''
        This function subtracts hits from a spacecraft's life.
        '''

        self.life -= hitpoints

    def translate_spacecraft(self, displacement_x, displacement_y):

        '''
        This method translate all the vertices of a spacecraft.
        It also translates self.x and self.y.
        Note that while self.speed determines how much a spacecraft will move, it's only used in
        the method that calculates the displacement. Meaning that this method can displace a spacecraft
        by anyamount.
        '''
        
        self.x += displacement_x
        self.y += displacement_y
        for vertex in self.vertices:
            vertex[0] = (vertex[0] + displacement_x) % WIDTH
            vertex[1] = (vertex[1] + displacement_y) % HEIGHT
            
    def rotate_spacecraft(self, angular_displacement):

        '''
        This method uses linear algebra to rotate the vertices by an angular_displacement using
        self.position as the rotation axis.
        It also unbounded by angle_speed as the translate_vertices method.
        '''

        cos = math.cos(angular_displacement)
        sin = math.sin(angular_displacement)
        for vertex in self.vertices:
            relative_x, relative_y = vertex[0] - self.x, vertex[1] - self.y
            relative_x, relative_y = cos*relative_x - sin*relative_y, sin*relative_x + cos*relative_y
            vertex[0], vertex[1] = relative_x + self.x, relative_y + self.y
        self.angle += angular_displacement % (2*math.pi)

    def get_vertices(self):

        '''
        This returns the spacecraft's vertices to be drawn on screen.
        '''

        return self.vertices


class Player(Spacecraft):


    def __init__(self, shape_function, color):

        Spacecraft.__init__(self, PLAYERX, PLAYERY, PLAYER_LIFE, PLAYER_SPEED, shape_function, color, PLAYER_ANGLE_SPEED, PLAYER_ANGLE)
        self.directions = [0, 0, 0, 0] # UP, DOWN, RIGHT, LEFT

    def move(self):

        if self.directions[0] or self.directions[1] or self.directions[2] or self.directions[3]:
            displacement_y = -(self.directions[0] - self.directions[1])*self.speed
            displacement_x = -(self.directions[2] - self.directions[3])*self.speed
            self.translate_spacecraft(displacement_x, displacement_y)
        
            
    def rotate(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        rel_x2, rel_y2 = self.vertices[0][0] - self.x, self.vertices[0][1] - self.y
        rel_x3, rel_y3 = rel_x2 - rel_x, rel_y2 - rel_y
        angular_displacement = (180 / math.pi) * math.atan2(rel_y3, rel_x3)
        self.rotate_spacecraft(angular_displacement)
