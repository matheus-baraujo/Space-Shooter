import pygame, sys, random
from classes import *
from constants import *
from shapes import *
from functions import *
from screens import *

def main():

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Shooter v1.0")
    pygame.mixer.init()
    start_screen(screen)

if __name__ == "__main__":

    main()

