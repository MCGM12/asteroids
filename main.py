import pygame
from constants import *
import circleshape
from player import Player

pygame.init()

def main():
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)


    the_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    while True:
        pygame.Surface.fill(screen, color=(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        the_player.draw(screen)
        
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    




if __name__ == "__main__":
    main()
