import pygame, sys
from classes import *
from constants import *
from shapes import *


def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = Player(shape1, WHITE) 

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            player.get_keyboard_input(event)

        player.update()
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":

    main()

