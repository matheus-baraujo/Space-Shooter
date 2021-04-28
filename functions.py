import classes
from constants import *
from shapes import *
import random

def create_enemy(score):

    level = min((5,score/2500))
    level = max((1, level))
    colors = PURPLE, ORANGE, CYAN, BLUE
    shapes = shape1,
    color = random.choice(colors)
    shape = random.choice(shapes)
    x_position = random.randrange(10, WIDTH-10)
    y_position = random.randrange(10, HEIGHT-10)
    life = random.randint(1, int(level))
    speed = random.uniform(0.01, 0.1) * level
    angle_speed = random.uniform(0.01, 0.02) * level
    max_distance = random.randint(150, 400)
    enemy = classes.Enemy(x_position, y_position, life, speed, shape, color, angle_speed, 0, max_distance)
    return enemy
