import pygame, sys, random
from classes import *
from constants import *
from shapes import *
from functions import *

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
   
    #transition elements
    i = 0
    fade = 1 # 0 = fading out, 1 = fading in
    locked_controls = False # lock the inputs during the screen transition
    nextScreen = 0 # control variable

    clock = pygame.time.Clock()

    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

    running = True

    #setting music channels for the start screen
    channel1 = pygame.mixer.Channel(0) 
    channel2 = pygame.mixer.Channel(1)

    start_screen_theme = pygame.mixer.Sound('sounds/start_screen_theme.mp3')
    hyperspace_jump = pygame.mixer.Sound('sounds/hyperspace_jump.mp3')

    channel1.play(start_screen_theme, -1)
    channel1.set_volume(0.4)

    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not locked_controls:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not locked_controls:
                #passes to the next screen
                nextScreen = 1
                i = 255
                locked_controls = True
                channel1.fadeout(4000)
                channel2.play(hyperspace_jump, 0)
                channel2.fadeout(3000)
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

    return personalization_screen(screen)    


def personalization_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    
    #elements utilized during the screen transition
    transition_slab = pygame.Surface(SIZE)
    transition_slab.fill(BLACK)
    transition_slab.set_alpha(0)
    transition_alpha = 0
    transition = False
    locked_controls = False

    #text input for nickname 
    font = pygame.font.SysFont('none', 50)
    text = "Anonymous"
    input_active = False
    text_color = (WHITE)

    #static elements
    player_customization = pygame.image.load(r'resources/player_customization.png') # 473 x 59 
    player_customization = player_customization.convert_alpha()

    title_nickname = pygame.image.load(r'resources/title_nickname.png') # 286 x 81
    title_nickname = pygame.transform.scale(title_nickname, (143,40)) # adjusting size
    title_nickname = title_nickname.convert_alpha()
    nickname_input_slab_size = 260,60
    nickname_input_slab = pygame.Surface(nickname_input_slab_size)
    nickname_input_slab.set_alpha(128)
    nickname_input_slab.fill(BLACK)

    title_color = pygame.image.load(r'resources/title_color.png') # 174 x 81
    title_color = pygame.transform.scale(title_color, (124, 40)) # adjusting size
    title_color = title_color.convert_alpha()
    color_output = WHITE #default of 5 colors [WHITE, CYAN, MAGENTA, ORANGE, RED]
    
    #color selection
    color_option1 = pygame.Surface((40,40))
    color_option1.fill(WHITE)
    highlight1 = pygame.Surface((50,50))
    highlight1.fill(YELLOW)
    highlight1.set_alpha(255)

    color_option2 = pygame.Surface((40,40))
    color_option2.fill(CYAN)
    highlight2 = pygame.Surface((50,50))
    highlight2.fill(YELLOW)
    highlight2.set_alpha(0)

    color_option3 = pygame.Surface((40,40))
    color_option3.fill(MAGENTA)
    highlight3 = pygame.Surface((50,50))
    highlight3.fill(YELLOW)
    highlight3.set_alpha(0)

    color_option4 = pygame.Surface((40,40))
    color_option4.fill(ORANGE)
    highlight4 = pygame.Surface((50,50))
    highlight4.fill(YELLOW)
    highlight4.set_alpha(0)

    color_option5 = pygame.Surface((40,40))
    color_option5.fill(RED)
    highlight5 = pygame.Surface((50,50))
    highlight5.fill(YELLOW)
    highlight5.set_alpha(0)

    #shape selection
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

    slab_size = WIDTH-80, HEIGHT-60
    slab = pygame.Surface(slab_size)
    slab.set_alpha(128)
    slab.fill(LIGHTGREY)

    clock = pygame.time.Clock()
    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)

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
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.MOUSEBUTTONDOWN and button_cancel_slab.get_alpha() == 128 and not locked_controls:
                running = False 
                #quit 
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and WIDTH/11 + 248 <= mouse_coord[0] <= WIDTH/11 + 448 and 175 <= mouse_coord[1] <= 235 and not locked_controls:
                input_active = True
                text = ""

            #receives the text input to create the nickname
            if event.type == pygame.KEYDOWN and input_active and not locked_controls:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    if(len(text) <= 9):
                       text += event.unicode

            #receives the color selection
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and WIDTH/11 + 234<=mouse_coord[0]<=WIDTH/11 + 274 and HEIGHT/1.8 + 5<=mouse_coord[1]<=HEIGHT/1.8 + 45:
                color_output = WHITE
                highlight1.set_alpha(255)
                highlight2.set_alpha(0)
                highlight3.set_alpha(0)
                highlight4.set_alpha(0)
                highlight5.set_alpha(0)
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and WIDTH/11 + 284<=mouse_coord[0]<=WIDTH/11 + 324 and HEIGHT/1.8 + 5<=mouse_coord[1]<=HEIGHT/1.8 + 45:
                color_output = CYAN
                highlight1.set_alpha(0)
                highlight2.set_alpha(255)
                highlight3.set_alpha(0)
                highlight4.set_alpha(0)
                highlight5.set_alpha(0)
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and WIDTH/11 + 334<=mouse_coord[0]<=WIDTH/11 + 374 and HEIGHT/1.8 + 5<=mouse_coord[1]<=HEIGHT/1.8 + 45:        
                color_output = MAGENTA
                highlight1.set_alpha(0)
                highlight2.set_alpha(0)
                highlight3.set_alpha(255)
                highlight4.set_alpha(0)
                highlight5.set_alpha(0)
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and WIDTH/11 + 384<=mouse_coord[0]<=WIDTH/11 + 424 and HEIGHT/1.8 + 5<=mouse_coord[1]<=HEIGHT/1.8 + 45:        
                color_output = ORANGE
                highlight1.set_alpha(0)
                highlight2.set_alpha(0)
                highlight3.set_alpha(0)
                highlight4.set_alpha(255)
                highlight5.set_alpha(0)
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and WIDTH/11 + 434<=mouse_coord[0]<=WIDTH/11 + 474 and HEIGHT/1.8 + 5<=mouse_coord[1]<=HEIGHT/1.8 + 45:        
                color_output = RED
                highlight1.set_alpha(0)
                highlight2.set_alpha(0)
                highlight3.set_alpha(0)
                highlight4.set_alpha(0)
                highlight5.set_alpha(255)        

            # receives the shape selection
            # arrow right button
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and shape_output < 2 and WIDTH/2 + 335 <=mouse_coord[0]<= WIDTH/2 + 381 and 245 <=mouse_coord[1]<= 325:
                shape_output += 1
            # arrow left button
            if event.type == pygame.MOUSEBUTTONDOWN and not locked_controls and shape_output > 0 and WIDTH/2 + 130 <=mouse_coord[0]<= WIDTH/2 + 176 and 245 <=mouse_coord[1]<= 325:    
                shape_output -= 1

            #passes to the next screen
            if event.type == pygame.MOUSEBUTTONDOWN and button_next_slab.get_alpha() == 128 and not locked_controls:
                transition = True
                locked_controls = True
            
        animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  

        screen.blit(slab, (40, 30))
        screen.blit(player_customization, (WIDTH/3.3, 50))

        screen.blit(title_nickname,(WIDTH/11 + 100, 180))
        screen.blit(nickname_input_slab,(WIDTH/11 + 248, 175))

        screen.blit(title_shape, (WIDTH/2 + 180, 180))
        if shape_output <= 0:
            button_selector_left.set_alpha(0)
        else:
            button_selector_left.set_alpha(255)

        if shape_output >= 2:
            button_selector_right.set_alpha(0)    
        else:
            button_selector_right.set_alpha(255)

        screen.blit(button_selector_left, (WIDTH/2 + 130, 245))
        screen.blit(button_selector_right, (WIDTH/2 + 190 + 145, 245))

        if(shape_output == 0):
            chosen_shape = shape1(selecting_shape_local[0], selecting_shape_local[1])
        elif(shape_output == 1):
            chosen_shape = shape2(selecting_shape_local[0], selecting_shape_local[1])
        elif(shape_output == 2):
            chosen_shape = star_shape(selecting_shape_local[0], selecting_shape_local[1])    
        
        pygame.draw.polygon(screen, color_output, chosen_shape)

        screen.blit(title_color, (WIDTH/11 + 100, HEIGHT/1.8))
        screen.blit(highlight1, (WIDTH/11 + 229, HEIGHT/1.8))
        screen.blit(color_option1, (WIDTH/11 + 234, HEIGHT/1.8 + 5))
        screen.blit(highlight2, (WIDTH/11 + 279, HEIGHT/1.8))
        screen.blit(color_option2, (WIDTH/11 + 284, HEIGHT/1.8 + 5))
        screen.blit(highlight3, (WIDTH/11 + 329, HEIGHT/1.8))
        screen.blit(color_option3, (WIDTH/11 + 334, HEIGHT/1.8 + 5))
        screen.blit(highlight4, (WIDTH/11 + 379, HEIGHT/1.8))
        screen.blit(color_option4, (WIDTH/11 + 384, HEIGHT/1.8 + 5))
        screen.blit(highlight5, (WIDTH/11 + 429, HEIGHT/1.8))
        screen.blit(color_option5, (WIDTH/11 + 434, HEIGHT/1.8 + 5))

        screen.blit(button_cancel_slab, (WIDTH/11-10, HEIGHT/1.2-10))
        screen.blit(button_cancel, (WIDTH/11, HEIGHT/1.2))

        screen.blit(button_next_slab, (WIDTH/1.2-10, HEIGHT/1.2-10))
        screen.blit(button_next, (WIDTH/1.2, HEIGHT/1.2))

        text_surf = font.render(text, True, text_color)
        screen.blit(text_surf, (WIDTH/11 + 253, 195))
        

        if (transition):
            transition_alpha += 5
            transition_slab.set_alpha(transition_alpha)
            if(transition_alpha >= 255):
                running = False

        screen.blit(transition_slab,(0, 0))

        pygame.display.update()
        clock.tick(30)

    return gameplay_screen(screen, text, color_output, shape_output)    


def gameplay_screen(screen, nickname, player_color, player_shape):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    clock = pygame.time.Clock()

    nickname = nickname
    player_color = player_color
    shape_selector = player_shape

    top_screen_bar = pygame.Surface((WIDTH, 50))
    top_screen_bar.fill(DARKGREY)

    life = pygame.image.load(r'resources/life_point.png') # 260 x 260
    life = pygame.transform.scale(life, (40,40))
    life = life.convert_alpha()

    score = 0

    font = pygame.font.SysFont(None, 40)
    nick = font.render(nickname, True, WHITE)
    lives = font.render("HP:", True, WHITE)
    points = font.render("Score:", True, WHITE)

    if(shape_selector == 0):
        player = Player(shape1, player_color)
    elif(shape_selector == 1):
        player = Player(shape2, player_color)
    elif(shape_selector == 2):
        player = Player(star_shape, player_color)    

    sprite_holder = Sprites(player)

    star_field_slow, star_field_medium, star_field_fast, star_field_shooting = generate_star_field(width, height)


    #setting music channels for the start screen
    channel1 = pygame.mixer.Channel(0) # background music
    channel2 = pygame.mixer.Channel(1) # player events
    channel3 = pygame.mixer.Channel(2) # enemies events
    channel4 = pygame.mixer.Channel(3) # screen transitions

    channel1.set_volume(0.3)
    channel2.set_volume(0.2)
    channel3.set_volume(0.5)
    channel4.set_volume(0.5)

    gameplay_music = pygame.mixer.Sound('sounds/gameplay_music.mp3')
    laser_shot = pygame.mixer.Sound('sounds/laser_shot_cut.mp3')

    channel1.play( gameplay_music, -1)
    

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                channel1.pause()
                pause_screen(screen)
                channel1.unpause()

            player.get_keyboard_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                channel2.play(laser_shot, 0)
                sprite_holder.player_shoot()

        if 1==random.randint(1,150) and sprite_holder.get_num_enemies()<5:
            enemy = create_enemy(sprite_holder.score)
            sprite_holder.add_enemy(enemy)

        sprite_holder.update()
        screen.fill(BLACK)

        animate_star_field(screen, star_field_slow, star_field_medium, star_field_fast, star_field_shooting, width, height)  

        sprite_holder.draw(screen)

        screen.blit(top_screen_bar, (0,0))
        screen.blit(nick, (5, 15))
        screen.blit(lives, (500, 15))

        scored_points = str(sprite_holder.score)
        scored = font.render(scored_points, True, WHITE)

        screen.blit(points, (1000, 15))
        screen.blit(scored, (1100,15))

        if player.life == 5:
            screen.blit(life, (WIDTH/12 + 630, 10))
            screen.blit(life, (WIDTH/12 + 585, 10))
            screen.blit(life, (WIDTH/12 + 540, 10))
            screen.blit(life, (WIDTH/12 + 495, 10))
            screen.blit(life, (WIDTH/12 + 450, 10))
        if player.life == 4:
            screen.blit(life, (WIDTH/12 + 585, 10))
            screen.blit(life, (WIDTH/12 + 540, 10))
            screen.blit(life, (WIDTH/12 + 495, 10))
            screen.blit(life, (WIDTH/12 + 450, 10))
        if player.life == 3:
            screen.blit(life, (WIDTH/12 + 540, 10))
            screen.blit(life, (WIDTH/12 + 495, 10))
            screen.blit(life, (WIDTH/12 + 450, 10))
        if player.life == 2:
            screen.blit(life, (WIDTH/12 + 495, 10))
            screen.blit(life, (WIDTH/12 + 450, 10))
        if player.life == 1:
            screen.blit(life, (WIDTH/12 + 450, 10))


        pygame.display.flip()
        clock.tick(30)


def pause_screen(screen):
    screen = screen
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    clock = pygame.time.Clock()

    pause_panel_size = width-840, height-250
    pause_panel = pygame.Surface(pause_panel_size)
    pause_panel.set_alpha(64)
    pause_panel.fill(LIGHTGREY)

    pause = pygame.image.load(r'resources/pause.png') # 160 x 60
    pause = pygame.transform.scale(pause, (186, 60))
    pause = pause.convert_alpha()

    button_resume = pygame.image.load(r'resources/button_resume.png') # 239 x 53
    button_resume = pygame.transform.scale(button_resume, (180, 40))
    button_resume = button_resume.convert_alpha()

    '''
    button_status = pygame.image.load(r'resources/button_status.png') # 249 x 81
    button_status = pygame.transform.scale(button_status, (184, 60))
    button_status = button_status.convert_alpha()
    '''

    button_quit = pygame.image.load(r'resources/button_quit.png') # 143 x 104
    button_quit = pygame.transform.scale(button_quit, (90, 65))
    button_quit = button_quit.convert_alpha()

    screen.blit(pause_panel, (WIDTH/2 - 220, 80))
    screen.blit(pause, (WIDTH/2 - 93, HEIGHT/6 + 30))
    
    running = True

    while running:

        mouse_coord = pygame.mouse.get_pos()
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.MOUSEBUTTONDOWN and WIDTH/2 - 45 < mouse_coord[0] < WIDTH/2 + 45 and HEIGHT/2.5 + 90 < mouse_coord[1] < HEIGHT/2.5 + 90 + 65:
                running = False 
                #quit 
                sys.exit() 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and WIDTH/2 - 90 < mouse_coord[0] < WIDTH/2 + 90 and  HEIGHT/2.5 + 30 < mouse_coord[1] < HEIGHT/2.5 + 30 + 40:
                #resume game
                running = False

        screen.blit(button_resume, (WIDTH/2 - 90, HEIGHT/2.5 + 30))
        screen.blit(button_quit, (WIDTH/2 - 45, HEIGHT/2.5 + 60 + 30))

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