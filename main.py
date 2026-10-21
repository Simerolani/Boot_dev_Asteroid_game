import pygame
#import SCREEN_HEIGHT, SCREEN_WIDTH from constants
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    #--- Instanciates the screen, clock an time delta
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
    clock = pygame.time.Clock()
    dt = 0.0
    #----Groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    #----Instanciates a Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        
        for inst in drawable:
            inst.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
