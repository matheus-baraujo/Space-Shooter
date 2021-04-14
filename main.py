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
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                angle = math.atan2(mouse_y - player.y, mouse_x - player.x)
                angle = angle * (180 / math.pi)
                player.rotate(angle)

        player_vertices = player.get_vertices()
        screen.fill(BLACK)
        pygame.draw.polygon(screen, WHITE, player_vertices)
        pygame.display.flip()

if __name__ == "__main__":

    main()

