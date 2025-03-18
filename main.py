# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while True:
        #This will check if the user has closed the window 
        #and exit the game loop if they do. It will make the 
        #window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0)) #fill the screen with a solid "black" color
        pygame.display.flip() #refresh the screen.



if __name__ == "__main__":
    main()