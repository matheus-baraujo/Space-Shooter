import pygame, sys
from classes import *
from constants import *
from shapes import *
from projectiles import *

def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = Player(shape1, WHITE) 
    player_projectiles = []

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            player.get_keyboard_input(event)
            player.get_mouse_input(event, player_projectiles)

        player.update()
        screen.fill(BLACK)
        player.draw(screen)
        projectile.projectiles_update(player_projectiles)
        pygame.display.flip()

if __name__ == "__main__":

    main()

