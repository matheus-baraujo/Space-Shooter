import pygame
import sys
from constants import *


class Spacecraft():


    '''
    This class will serve as a parent class for both Player class and Enemy class.
    Its purpose is to deal with basic movement that both the Player spacecraft and Enemy spacecraft will
    have to display.
    '''

    def __init__(self, x_position, y_position, life, speed, shape_function, color, angle_speed, angle = 0):

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
        
        self.position = self.x, self.y = x_position, y_position
        self.vertices = shape_function(self.position)
        self.life = life
        self.speed = speed
        self.angle = angle
        self.angle_speed = angle_speed
        self.rotate_vertices(self.angle)

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

    def translate_vertices(self, displacement):

        '''
        This method translate all the vertices of a spacecraft.
        Note that while self.speed determines how much a spacecraft will move, it's only used in
        the method that calculates the displacement. Meaning that this method can displace a spacecraft
        by anyamount.
        '''

        for vertex in self.vertices:
            vertex[0], vertex[1] += displacement[0], displacement[1]
            vertex[0] %= WIDTH
            vertex[0] %= HEIGHT
            
    def rotate_vertices(self, angular_displacement):

        '''
        This method uses linear algebra to rotate the vertices by an angular_displacement using
        self.position as the rotation axis.
        It also unbounded by angle_speed as the translate_vertices method.
        '''

        cos = math.cos(angular_displacement)
        sin = math.sin(angular_displacement)
        for vertex in self.vertices:
            relativex, relativey = vertex[0] - self.x, vertex[1] - self.y
            relativex, relativey = cos*relativex - sin*relativey, sin*relativex + cos*relativey
            vertex[0], vertex[1] = relativex + self.x, relativey + self,y
        self.angle += angular_displacement % (2*math.pi)

    def get_vertices(self):

        '''
        This returns the spacecraft's vertices to be drawn on screen.
        '''

        return self.vertices


class PlayerObject():


    def __init__(self, width, height):

        initial_vertex1 = [width/2, height/2]
        initial_vertex2 = [width/2 - 10,height/2 + 20]
        initial_vertex3 = [width/2 + 10,height/2 + 20]
        self.vertices = [initial_vertex1, initial_vertex2, initial_vertex3]
        self.life = 5

        self.surface = pygame.image.load() #adicionar uma imagem pra ser o player
        self.rotated_surface = self.surface.copy()
        self.directions = [False, False, False, False] # UP, DOWN, RIGHT, LEFT
        self.speed = 0.1

    def is_dead(self):

        if self.life < 1:
            return False
        else:
            return True

    def moves(self):
        if self.directions[0] || self.directions[1] or self.directions[2] || self.directions[3]:
            self.y += (self.directions[0] - self.directions[1])*self.speed
            self.x += (self.directions[2] - self.directions[3])*self.speed
            
    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.position)       
            
    def get_vertices(self):
        return self.vertices

    def update_vertices(self, new_vertices):
        self.vertices = new_vertices  