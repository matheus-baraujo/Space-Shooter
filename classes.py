import pygame
import sys

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