import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()

    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)


    

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill(), asteroid.split()
            
        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        
        


if __name__ == "__main__":
    main()