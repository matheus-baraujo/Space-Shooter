import classes, pygame
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
    speed = random.uniform(level/10, level/5)
    angle_speed = min((1, random.uniform(level/20, level/10)))
    max_distance = random.randint(150, 300)
    min_distance = max_distance - 50
    max_shoot = random.randint(25, 35)
    enemy = classes.Enemy(x_position, y_position, life, speed, shape, color, angle_speed, 0, max_distance, min_distance, max_shoot)
    return enemy

def generate_star_field(width, height):
    width = width
    height = height
    
    #create the locations of the stars for when we animate the background
    star_field_slow = []
    star_field_medium = []
    star_field_fast = []
    star_field_shooting = []

    for slow_stars in range(60): #creating the locations of the stars
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_slow.append([star_loc_x, star_loc_y]) 

    for medium_stars in range(40):
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_medium.append([star_loc_x, star_loc_y])

    for fast_stars in range(20):
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_fast.append([star_loc_x, star_loc_y])
    
    for shooting_stars in range(1):
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_shooting.append([star_loc_x, star_loc_y])

    return   star_field_slow, star_field_medium, star_field_fast, star_field_shooting  

def animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height):

    width = width
    height = height

    star_field_slow = star_field_slow
    star_field_medium = star_field_medium
    star_field_fast = star_field_fast
    star_field_shooting = star_field_shooting

    #animating the background with stars
    for star in star_field_slow:
        star[1] += 1
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, DARKGREY, star, 3)

    for star in star_field_medium:
        star[1] += 4
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, CYAN, star, 2)

    for star in star_field_fast:
        star[1] += 8
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, YELLOW, star, 1)

    for star in star_field_shooting:
        star[0] += 16
        star[1] += 16
        if star[0] > width:
            star[0] = random.randrange(-20, -5)
            star[1] = random.randrange(0, height)
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, MAGENTA, star, 1)     

def animate_star_field_combat(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height):

    width = width
    height = height

    star_field_slow = star_field_slow
    star_field_medium = star_field_medium
    star_field_fast = star_field_fast
    star_field_shooting = star_field_shooting

    #animating the background with stars
    for star in star_field_slow:
        star[1] += 1
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, DARKGREY, star, 1)

    for star in star_field_medium:
        star[1] += 4
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, CYAN, star, 1)

    for star in star_field_fast:
        star[1] += 8
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, YELLOW, star, 1)

    for star in star_field_shooting:
        star[0] += 16
        star[1] += 16
        if star[0] > width:
            star[0] = random.randrange(-20, -5)
            star[1] = random.randrange(0, height)
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, MAGENTA, star, 1)     