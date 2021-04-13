import pygame, sys

SIZE = WIDTH, HEIGHT = 960, 640
BLACK = 0, 0, 0
WHITE = 255, 255, 255


def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    initialp1 = [WIDTH/2, HEIGHT/2]
    initialp2 = [WIDTH/2 - 10,HEIGHT/2 + 20]
    initialp3 = [WIDTH/2 + 10,HEIGHT/2 + 20]
    player_initial_position = [initialp1, initialp2, initialp3]

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: sys.exit()

        screen.fill(BLACK)
        pygame.draw.polygon(screen, WHITE, player_initial_position)
        pygame.display.flip()

if __name__ == "__main__":

    main()

