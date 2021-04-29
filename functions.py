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
    life = random.randint(1, level)
    
    if(life <= 1):
        colors = GREEN, PURPLE, BLUE
    else:
        colors = RED, ORANGE

    color = random.choice(colors)
    speed = 10*random.uniform(level/10, level/5)
    angle_speed = min((1, random.uniform(level/20, level/10)))
    max_distance = random.randint(150, 300)
    min_distance = max_distance - 50
    max_shoot = random.randint(25, 35)
    enemy = classes.Enemy(x_position, y_position, life, speed, shape, color, angle_speed, 0, max_distance, min_distance, max_shoot)
    return enemy
