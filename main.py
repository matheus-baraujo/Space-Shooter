import pygame, sys
from classes import *

SIZE = WIDTH, HEIGHT = 960, 640
BLACK = 0, 0, 0
WHITE = 255, 255, 255


def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = PlayerObject(WIDTH, HEIGHT)

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: sys.exit()

        player_vertices = player.get_vertices()
        screen.fill(BLACK)
        pygame.draw.polygon(screen, WHITE, player_vertices)
        pygame.display.flip()

if __name__ == "__main__":

    main()

