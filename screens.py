import pygame, sys, random
from classes import *
from constants import *
from shapes import *

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

def start_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    logo = pygame.image.load(r'resources/logo.png') # 512 x 104 
    logo = logo.convert_alpha()

    start_message = pygame.image.load(r'resources/start_message.png') # 591 x 46
    start_message = pygame.transform.scale(start_message, (300, 20)) # adjusting the size
    start_message = start_message.convert_alpha()
    i = 0
    fade = 1 # 0 = fading out, 1 = fading in

    nextScreen = 0 # control variable

    clock = pygame.time.Clock()

    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #passes to the next screen
                nextScreen = 1
                i = 255
                #running = False 

        screen.fill(BLACK)

        animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  
        
        if(nextScreen == 0):
            if fade == 1:
                i += 5
            else:
                i -= 5   

            if(i >= 255):
                fade = 0
            elif(i <= 0):
                fade = 1            

            screen.blit(logo, (WIDTH/3.3, HEIGHT/4))
            start_message.set_alpha(i)
            screen.blit(start_message, (WIDTH/2.7, HEIGHT/1.5))
        else:
            i -= 5  
            logo.set_alpha(i)
            start_message.set_alpha(i)
            screen.blit(logo, (WIDTH/3.3, HEIGHT/4))
            screen.blit(start_message, (WIDTH/2.7, HEIGHT/1.5))
            if(i <= 0):
                running = False

        #redraw everything we've asked pygame to draw
        pygame.display.update()

        #set frames per second
        clock.tick(30)


def personalization_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    
    clock = pygame.time.Clock()
    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

    running = True

    while running:
        screen.fill(BLACK)

        for star in star_field_slow:
            pygame.draw.polygon(screen, DARKGREY, star_shape(star[0], star[1]))

        for star in star_field_medium:
            pygame.draw.polygon(screen, CYAN, star_shape(star[0], star[1]))

        for star in star_field_fast:
            pygame.draw.polygon(screen, YELLOW, star_shape(star[0], star[1]))

        for star in star_field_shooting:
            pygame.draw.polygon(screen, MAGENTA, star_shape(star[0], star[1])) 


        pygame.display.update()
        clock.tick(30)


#def gameplay_screen:

#def pause_screen:

#def ending_screen:     