import classes
from constants import *
from shapes import *
import random

def create_enemy(score):

    level = int(score/1500)
    level = max((1, level))
    shape = enemy_shape
    x_position = random.randrange(10, WIDTH-10)
    y_position = random.randrange(60, HEIGHT-10)
    life = random.randint(1, int(level))
    
    if(life <= 1):
        colors = GREEN, PURPLE, BLUE
    else:
        colors = RED, ORANGE

    color = random.choice(colors)
    speed = random.uniform(0.2, 0.5) * level
    angle_speed = random.uniform(0.1, 0.2) * level
    max_distance = random.randint(150, 400)
    max_shoot = random.randint(20, 30)
    enemy = classes.Enemy(x_position, y_position, life, speed, shape, color, angle_speed, 0, max_distance, max_shoot)
    return enemy
