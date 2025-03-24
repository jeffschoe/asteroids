import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #get a new GUI window:
    clock = pygame.time.Clock() #create an object to help track time
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #create player in middle of screen

    dt = 0 #delta time

    while True:
        for event in pygame.event.get(): #This will check if the user has closed the window 
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black") #fill the screen with a solid "black" color
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() #refresh the screen.

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000 #Pause the game loop until 1/60th of a second has passed.        


if __name__ == "__main__":
    main()