import pygame, sys
from classes import *
from constants import *
from shapes import *
from projectiles import *
from screens import *

def main():

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Shooter v1.0")
    
    pygame.mixer.init()
    start_screen(screen)
    
    '''
    player = Player(shape1, WHITE) 
    sprite_holder = Sprites()

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            player.get_keyboard_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                projectile = player.shoot(PROJECTILE_SPEED, YELLOW)
                sprite_holder.add_projectile(projectile)

        player.update()
        sprite_holder.update()
        screen.fill(BLACK)
        player.draw(screen)
        sprite_holder.draw(screen)
        pygame.display.flip()
    '''    

if __name__ == "__main__":

    main()

