import pygame
import sys
#import SCREEN_HEIGHT, SCREEN_WIDTH from constants
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    #---ISTANCIANTES THE SCREEN, CLOCK, AND TIME DELTA
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
    clock = pygame.time.Clock()
    dt = 0.0
    
    #----GROUPS
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    #----ISTANCIANTES THE OBJECTS
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #----GAMELOOP
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for ast in asteroids:
            #Check for Player / Asteroid Collision
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            #Check for Bullet / Asteroid Collision
            for bul in shots:
                if bul.collides_with(ast):
                    log_event("asteroid_shot")
                    bul.kill()
                    ast.split()
        screen.fill("black")
        
        for inst in drawable:
            inst.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
