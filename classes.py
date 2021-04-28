import pygame, random
import sys
import math
from constants import *
from functions import *


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
        self.color = color
        self.hitbox = pygame.Rect(0,0,0,0)

    def is_dead(self):

        '''
        This methods checks if a spacecraft life has reached zero.
        '''

        if self.life < 1:
            return True
        else:
            return False

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
            vertex[0] = (vertex[0] + displacement_x)
            vertex[1] = (vertex[1] + displacement_y)
            
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

    def draw(self, screen):

        self.hitbox = pygame.draw.polygon(screen, self.color, self.vertices)

    def shoot(self, speed, color):

        ''' this function creates a bullet in front of the ship, providing it with speed, direction and size '''

        direction = [self.vertices[0][0] - self.x, self.vertices[0][1] - self.y]
        direction = tuple(x*(1/math.sqrt(direction[0]**2 + direction[1]**2)) for x in direction)
        return Projectile(self.vertices[0][0], self.vertices[0][1], speed, color, PROJECTILE_RADIUS, direction)

    def get_position(self):

        return self.x, self.y


class Player(Spacecraft):


    def __init__(self, shape_function, color):

        Spacecraft.__init__(self, PLAYERX, PLAYERY, PLAYER_LIFE, PLAYER_SPEED, shape_function, color, PLAYER_ANGLE_SPEED, PLAYER_ANGLE)
        self.directions = [0, 0, 0, 0] # UP, DOWN, RIGHT, LEFT
        self.has_shield = False

    def register_hit(self, hitpoints=1):

        '''
        This function subtracts hits from a spacecraft's life.
        '''
        if self.has_shield:
            self.has_shield = False
        else:
            self.life -= hitpoints

    def heal(self):

        self.life = min((5, self.life+1))

    def get_keyboard_input(self, event):

        if event.type == pygame.KEYDOWN: #buttons pressed
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_w:
                self.directions[0] = 1
            if event.key == pygame.K_s:
                self.directions[1] = 1
            if event.key == pygame.K_a:
                self.directions[2] = 1
            if event.key == pygame.K_d:
                self.directions[3] = 1       

        elif event.type == pygame.KEYUP: #buttons not pressed
            if event.key == pygame.K_w:
                self.directions[0] = 0
            if event.key == pygame.K_s:
                self.directions[1] = 0
            if event.key == pygame.K_a:
                self.directions[2] = 0
            if event.key == pygame.K_d:
                self.directions[3] = 0

    def get_mouse_input(self, event, array):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.shoot(array)           

    def move(self):

        if self.directions[0] or self.directions[1] or self.directions[2] or self.directions[3]:
            displacement_y = -(self.directions[0] - self.directions[1])*self.speed
            displacement_x = -(self.directions[2] - self.directions[3])*self.speed
            self.translate_spacecraft(displacement_x, displacement_y)
        
       
    def rotate(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        rel_x2, rel_y2 = self.vertices[0][0] - self.x, self.vertices[0][1] - self.y

        angular_displacement = math.atan2(rel_x2, rel_y2) - math.atan2(rel_x, rel_y)
        angular_displacement *= self.angle_speed
        self.rotate_spacecraft(angular_displacement)

    def update(self):

        self.move()
        self.rotate()

    def draw(self, screen):

        if not self.has_shield:
            self.hitbox = pygame.draw.polygon(screen, self.color, self.vertices)
        else:
            pygame.draw.polygon(screen, self.color, self.vertices)
            self.hitbox = pygame.draw.circle(screen, BLUE, (self.x, self.y), 25, 5)

    
class Enemy(Spacecraft):


    def __init__(self, x_position, y_position, life, speed, shape_function, color, angle_speed, angle, max_distance_to_player, shoot_max):

        Spacecraft.__init__(self, x_position, y_position, life, speed, shape_function, color, angle_speed, angle)
        self.max_distance = max_distance_to_player
        self.shoot_count = 0
        self.shoot_max = shoot_max
        self.shoot_lock = False

    def rotate(self, x_player, y_player):

        rel_x, rel_y = x_player - self.x, y_player - self.y
        rel_x2, rel_y2 = self.vertices[0][0] - self.x, self.vertices[0][1] - self.y
        angular_displacement = math.atan2(rel_x2, rel_y2) - math.atan2(rel_x, rel_y)
        angular_displacement *= self.angle_speed
        self.rotate_spacecraft(angular_displacement)

    def move(self, x_player, y_player):

        rel_x, rel_y = x_player - self.x, y_player - self.y
        distance = math.sqrt(rel_x**2 + rel_y**2)
        if distance>self.max_distance:
            displacement_x = self.speed*rel_x/distance
            displacement_y = self.speed*rel_y/distance
            self.translate_spacecraft(displacement_x, displacement_y)
        elif distance<self.max_distance:
            displacement_x = -self.speed*rel_x/distance
            displacement_y = -self.speed*rel_y/distance
            self.translate_spacecraft(displacement_x, displacement_y)

    def update(self, x_player, y_player):

        self.move(x_player, y_player)
        self.rotate(x_player, y_player)


class Projectile():

    def __init__(self, x_position, y_position, speed, color, radius, direction):

        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.color = color
        self.radius = radius 
        self.direction = direction
        self.hitbox = pygame.Rect(0,0,0,0)

    def draw(self, screen):

        self.hitbox = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):

        self.x += self.direction[0] * self.speed  
        self.y += self.direction[1] * self.speed

    def is_out_of_bound(self):

        if self.x<0 or self.x>WIDTH or self.y<0 or self.y>HEIGHT:
            return True
        else:
            return False


class Sprites():


    def __init__(self, player):

        self.enemy_projectiles = []
        self.powerups = []
        self.player_projectiles = []
        self.enemies = []
        self.player = player
        self.score = 0

    def genarate_objects(self):

        if 1==random.randint(1,50) and len(self.enemies)<5:
            enemy = create_enemy(self.score)
            self.enemies.append(enemy)

        if 1==random.randint(1, 300):
            powerup_type = random.choice((0,1))
            x_position = random.randint(0, WIDTH)
            y_position = random.randint(0, HEIGHT)
            power_up = PowerUp(x_position, y_position, powerup_type)
            self.powerups.append(power_up)

    def get_keyboard_input(self, event):

        self.player.get_keyboard_input(event)

    def player_shoot(self):

        projectile = self.player.shoot(PROJECTILE_SPEED, YELLOW)
        self.player_projectiles.append(projectile)

    def update_projectiles(self):

        for projectile in self.player_projectiles:
            projectile.move()
            if projectile.is_out_of_bound():
                self.player_projectiles.remove(projectile)
                del projectile
                continue
            colliding_enemy_index = projectile.hitbox.collidelist([x.hitbox for x in self.enemies])
            if colliding_enemy_index==-1:
                continue
            else:
                self.enemies[colliding_enemy_index].register_hit()
                self.player_projectiles.remove(projectile)
                del projectile
            
        for projectile in self.enemy_projectiles:
            projectile.move()
            if projectile.is_out_of_bound():
                self.enemy_projectiles.remove(projectile)
                del projectile
                continue
            if projectile.hitbox.colliderect(self.player.hitbox):
                self.player.register_hit()
                self.enemy_projectiles.remove(projectile)
                del projectile
                continue

    def update_enemies(self):

        x_pos, y_pos = self.player.get_position()
        for enemy in self.enemies:
            enemy.update(x_pos, y_pos)
            if enemy.is_dead():
                self.enemies.remove(enemy)
                self.score += 50
                del enemy
                continue
            if not enemy.shoot_lock:
                enemy_projectile = enemy.shoot(PROJECTILE_SPEED/3, RED)
                self.enemy_projectiles.append(enemy_projectile)
                enemy.shoot_lock = True
                enemy.shoot_count = 0
            elif enemy.shoot_count < enemy.shoot_max:
                enemy.shoot_count += 1
            else:
                enemy.shoot_lock = False

    def update_player(self):

        self.player.update()
        for powerup in self.powerups:
            if powerup.hitbox.colliderect(self.player.hitbox):
                if powerup.type==0:
                    self.player.heal()
                elif powerup.type==1:
                    self.player.has_shield = True
                self.powerups.remove(powerup)
                del powerup

    def update(self):

        self.update_player()
        self.update_projectiles()
        self.update_enemies()

    def draw(self, screen):

        if not self.player.is_dead():
            self.player.draw(screen)

        for projectile in self.player_projectiles:
            projectile.draw(screen)

        for projectile in self.enemy_projectiles:
            projectile.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        for powerup in self.powerups:
            powerup.draw(screen)


class PowerUp():

    def __init__(self, x_position, y_position, powerup_type):

        self.x = x_position
        self.y = y_position
        self.type = powerup_type
        self.color = {0: RED, 1: BLUE}[powerup_type]
        self.vertices = self.shape()
        self.hitbox = pygame.Rect(0,0,0,0)
    
    def shape(self):

        vertex1 = [self.x+3, self.y+3]
        vertex2 = [self.x+3, self.y+10]
        vertex3 = [self.x-3, self.y+10]
        vertex4 = [self.x-3, self.y+3]
        vertex5 = [self.x-10, self.y+3]
        vertex6 = [self.x-10, self.y+-3]
        vertex7 = [self.x-3, self.y-3]
        vertex8 = [self.x-3, self.y-10]
        vertex9 = [self.x+3, self.y-10]
        vertex10 = [self.x+3, self.y-3]
        vertex11 = [self.x+10, self.y-3]
        vertex12 = [self.x+10, self.y+3]

        return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, vertex9, vertex10, vertex11, vertex12]

    def draw(self, screen):

        self.hitbox = pygame.draw.polygon(screen, self.color, self.vertices)