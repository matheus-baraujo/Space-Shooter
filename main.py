import pygame, sys
from classes import *


def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = PlayerObject(WIDTH, HEIGHT)

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            elif event.type == pygame.KEYDOWN: #buttons pressed
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_w:
                    player.directions[0] = 1
                if event.key == pygame.K_s:
                    player.directions[1] = 1
                if event.key == pygame.K_a:
                    player.directions[2] = 1
                if event.key == pygame.K_d:
                    player.directions[3] = 1

            elif event.type == pygame.KEYUP: #buttons not pressed
                if event.key == pygame.K_w:
                    player.directions[0] = 0
                if event.key == pygame.K_s:
                    player.directions[1] = 0
                if event.key == pygame.K_a:
                    player.directions[2] = 0
                if event.key == pygame.K_d:
                    player.directions[3] = 0

            elif event.type == pygame.MOUSEMOTION:
                player.rotate()

        player_vertices = player.get_vertices()
        screen.fill(BLACK)
        pygame.draw.polygon(screen, WHITE, player_vertices)
        player.moves()
        pygame.display.flip()

if __name__ == "__main__":

    main()

