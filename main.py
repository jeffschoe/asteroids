# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() #create an object to help track time
    dt = 0 #delta time

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) #create player in middle of screen

    #game loop
    while True:
        #This will check if the user has closed the window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0,0,0)) #fill the screen with a solid "black" color
        player.draw(screen)
        
        pygame.display.flip() #refresh the screen.
        dt = clock.tick(60)/1000 #Pause the game loop until 1/60th of a second has passed.
        


if __name__ == "__main__":
    main()