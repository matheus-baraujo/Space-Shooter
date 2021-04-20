import pygame, sys, random
from classes import *
from constants import *
from shapes import *

def start_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    
    clock = pygame.time.Clock()

    #create the locations of the stars for when we animate the background
    star_field_slow = []
    star_field_medium = []
    star_field_fast = []
    #star_field_comets = []

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
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                #quit 
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #passes to the next screen
                running = False 

        screen.fill(BLACK)

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

        #redraw everything we've asked pygame to draw
        pygame.display.flip()

        #set frames per second
        clock.tick(30)

    