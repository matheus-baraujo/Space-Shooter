import pygame, sys
from classes import *
from constants import *
from shapes import *
from projectiles import *
from screens import *

def main():

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    start_screen(screen)
    player = Player(shape1, WHITE) 
    sprites_object = Sprites()

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            player.get_keyboard_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(sprites_object)  

        player.update()
        screen.fill(BLACK)
        player.draw(screen)
        sprites_object.update(screen)
        pygame.display.flip()

if __name__ == "__main__":

    main()

