import sys

import pygame

from globals import *


class App:
    def __init__(self, caption: str = '') -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
            self.screen.fill('lightblue')
            pygame.display.update()
            dt = self.clock.tick(FRAMERATE)

    def close(self) -> None:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = App('Game Jam')
    game.run()
