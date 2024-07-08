import pygame
import sys
from settings import *

class Game:

    def __init__(self):
        
        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Soul Exorcist')
        self.clock = pygame.time.Clock()
        
        # Initialize Level

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)
        
if __name__ == '__main__':
    game = Game()
    game.run()