from tkinter.tix import Tree
import pygame, sys
from level import Level
from settings import *
from debug import debug

class Game():

    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Apply images and set up name
        pygame.display.set_caption('Tower adventure')
        icon = pygame.image.load('images/tower.png')
        pygame.display.set_icon(icon)

    def run(self):
        while True:
            for event in pygame.event.get():
                # Quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()