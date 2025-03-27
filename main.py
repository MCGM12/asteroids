import pygame
from constants import *
import circleshape
import player

pygame.init()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    the_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        pygame.Surface.fill(screen, color=(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000
        the_player.update(dt)
        the_player.draw(screen)
        pygame.display.flip()
    




if __name__ == "__main__":
    main()
