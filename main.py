import pygame, sys, random
from classes import *
from constants import *
from shapes import *
from functions import *

def main():


    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    player = Player(shape1, WHITE) 
    sprite_holder = Sprites(player)
    score = 0

    while True:

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT: 
                sys.exit()

            sprite_holder.get_keyboard_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_holder.player_shoot()
        
        if 1==random.randint(1,800) and sprite_holder.get_num_enemies()<=10:
            enemy = create_enemy(score)
            sprite_holder.add_enemy(enemy)

        sprite_holder.update()
        screen.fill(BLACK)
        sprite_holder.draw(screen)
        pygame.display.flip()
        score +=1

if __name__ == "__main__":

    main()

