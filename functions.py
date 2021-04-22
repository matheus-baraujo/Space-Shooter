from classes import *
from constants import *
from shapes import *
import random

def create_enemy():

    colors = PURPLE, ORANGE, CYAN, BLUE
    shapes = shape1,
    color = random.choice(colors)
    shape = random.choice(shapes)
    x_position = random.randrange(10, WIDTH-10)
    y_position = random.randrange(10, HEIGHT-10)
    life = random.randint(1, 4)
    speed = random.uniform(0.4, 0.6)
    angle_speed = random.uniform(0.9, 1.1)
    max_distance = random.randint(100, 300)
    enemy = Enemy(x_position, y_position, life, speed, shape, color, angle_speed, 0, max_distance)
    return enemy
