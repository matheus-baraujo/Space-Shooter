import pygame, sys
from classes import *
from constants import *
from shapes import *

def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = Player(shape1, WHITE) 
    sprite_holder = Sprites(player)

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            sprite_holder.get_keyboard_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_holder.player_shoot()

        sprite_holder.update()
        screen.fill(BLACK)
        sprite_holder.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":

    main()

