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

'''
def circulate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height):

    width = width
    height = height
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

    star_field_slow = star_field_slow
    star_field_medium = star_field_medium
    star_field_fast = star_field_fast
    star_field_shooting = star_field_shooting
'''


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

            if(i >= 128):
                for speed in range(255-i):
                    animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  
            else:
                for speed in range(i):
                    animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  


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
    
    player_customization = pygame.image.load(r'resources/player_customization.png') # 473 x 59 
    player_customization = player_customization.convert_alpha()

    title_nickname = pygame.image.load(r'resources/title_nickname.png') # 286 x 81
    title_nickname = pygame.transform.scale(title_nickname, (143,40)) # adjusting size
    title_nickname = title_nickname.convert_alpha()
    nickname_input_slab_size = 200,60
    nickname_input_slab = pygame.Surface(nickname_input_slab_size)
    nickname_input_slab.set_alpha(128)
    nickname_input_slab.fill(BLACK)
    nickname_input = []
    nickname_output = 'Player' #default

    title_color = pygame.image.load(r'resources/title_color.png') # 174 x 81
    title_color = pygame.transform.scale(title_color, (124, 40)) # adjusting size
    title_color = title_color.convert_alpha()
    color_output = 0 #default of 5 colors [WHITE, GREEN, MAGENTA, ]

    title_shape = pygame.image.load(r'resources/title_shape.png') # 209 x 104
    title_shape = pygame.transform.scale(title_shape, (145, 50))
    title_shape = title_shape.convert_alpha()
    selecting_shape_local = WIDTH/2 + 180 + 80, 285
    shape_output = 0 #default of 3 shapes [0, 1, 2]

    button_next = pygame.image.load(r'resources/button_next.png') # 103 x 42
    button_next = button_next.convert_alpha()
    button_next_slab_size = 123, 62
    button_next_slab = pygame.Surface(button_next_slab_size)
    button_next_slab.set_alpha(0)
    button_next_slab.fill(BLACK)

    button_cancel = pygame.image.load(r'resources/button_cancel.png') # 133 x 42
    button_cancel = button_cancel.convert_alpha()
    button_cancel_slab_size = 153, 62
    button_cancel_slab = pygame.Surface(button_cancel_slab_size)
    button_cancel_slab.set_alpha(0)
    button_cancel_slab.fill(BLACK) 

    button_selector_right = pygame.image.load(r'resources/button_selector_right.png') # 46 x 80
    button_selector_right = button_selector_right.convert_alpha()

    button_selector_left = pygame.image.load(r'resources/button_selector_left.png') # 46 x 80
    button_selector_left = button_selector_left.convert_alpha()


    clock = pygame.time.Clock()
    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

    slab_size = WIDTH-80, HEIGHT-60
    slab = pygame.Surface(slab_size)
    slab.set_alpha(128)
    slab.fill(LIGHTGREY)

    running = True

    while running:
        screen.fill(BLACK)
        
        mouse_coord = pygame.mouse.get_pos()
        
        if( WIDTH/1.2 <= mouse_coord[0] <= WIDTH/1.2 + 103 and  HEIGHT/1.2 <= mouse_coord[1] <= HEIGHT/1.2 + 42):
            #mouse hover on next button
            button_next_slab.set_alpha(128)
        else:
            button_next_slab.set_alpha(0)    

        if( WIDTH/11 <= mouse_coord[0] <= WIDTH/11 + 133 and HEIGHT/1.2 <= mouse_coord[1] <= HEIGHT/1.2 + 42):
            #mouse hover on cancel button
            button_cancel_slab.set_alpha(128)
        else:
            button_cancel_slab.set_alpha(0)    

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.MOUSEBUTTONDOWN and button_cancel_slab.get_alpha() == 128:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN and button_next_slab.get_alpha() == 128:
                #passes to the next screen
                running = False
            
        animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  

        screen.blit(slab, (40, 30))
        screen.blit(player_customization, (WIDTH/3.3, 50))

        screen.blit(title_nickname,(WIDTH/11 + 100, 180))
        screen.blit(nickname_input_slab,(WIDTH/11 + 248, 175))

        screen.blit(title_shape, (WIDTH/2 + 180, 180))
        screen.blit(button_selector_left, (WIDTH/2 + 130, 245))
        screen.blit(button_selector_right, (WIDTH/2 + 190 + 145, 245))
        chosen_shape = shape1(selecting_shape_local[0], selecting_shape_local[1])
        pygame.draw.polygon(screen, WHITE, chosen_shape)

        screen.blit(title_color, (WIDTH/11 + 100, HEIGHT/1.8))



        screen.blit(button_cancel_slab, (WIDTH/11-10, HEIGHT/1.2-10))
        screen.blit(button_cancel, (WIDTH/11, HEIGHT/1.2))

        screen.blit(button_next_slab, (WIDTH/1.2-10, HEIGHT/1.2-10))
        screen.blit(button_next, (WIDTH/1.2, HEIGHT/1.2))

        pygame.display.update()
        clock.tick(30)


#def gameplay_screen(screen, player, nickname, score):


def pause_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    clock = pygame.time.Clock()

    pause_panel_size = width-640, height-100
    pause_panel = pygame.Surface(pause_panel_size)
    pause_panel.set_alpha(64)
    pause_panel.fill(LIGHTGREY)

    pause = pygame.image.load(r'resources/pause.png') # 160 x 60
    pause = pygame.transform.scale(pause, (186, 60))
    pause = pause.convert_alpha()

    button_resume = pygame.image.load(r'resources/button_resume.png') # 239 x 53
    button_resume = pygame.transform.scale(button_resume, (180, 40))
    button_resume = button_resume.convert_alpha()

    button_status = pygame.image.load(r'resources/button_status.png') # 249 x 81
    button_status = pygame.transform.scale(button_status, (184, 60))
    button_status = button_status.convert_alpha()

    button_quit = pygame.image.load(r'resources/button_quit.png') # 143 x 104
    button_quit = pygame.transform.scale(button_quit, (90, 65))
    button_quit = button_quit.convert_alpha()

    screen.blit(pause_panel, (WIDTH/2 - 320, 50))
    screen.blit(pause, (WIDTH/2 - 93, HEIGHT/6))
    
    running = True

    while running:

        mouse_coord = pygame.mouse.get_pos()

        #if ( WIDTH/2 - 90 < mouse_coord[0] < WIDTH/2 + 45 and  HEIGHT/2.5 < mouse_coord[1] < HEIGHT/2.5 + 40):


        #if ( WIDTH/2 - 92 < mouse_coord[0] < WIDTH/2 + 45 and  HEIGHT/2.5 + 60 < mouse_coord[1] < HEIGHT/2.5 + 60 + 60):
            

        #if ( WIDTH/2 - 45 < mouse_coord[0] < WIDTH/2 + 45 and HEIGHT/2.5 + 140 < mouse_coord[1] < HEIGHT/2.5 + 140 + 65):        
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #passes to the next screen
                running = False

        screen.blit(button_resume, (WIDTH/2 - 90, HEIGHT/2.5))
        screen.blit(button_status, (WIDTH/2 - 92, HEIGHT/2.5 + 60))
        screen.blit(button_quit, (WIDTH/2 - 45, HEIGHT/2.5 + 140))

        pygame.display.update()
        clock.tick(30)
    

def ending_screen(screen, nickname, score):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    clock = pygame.time.Clock()
    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN and button_next_slab.get_alpha() == 128:
                #passes to the next screen
                running = False

        animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  

        pygame.display.update()
        clock.tick(30)