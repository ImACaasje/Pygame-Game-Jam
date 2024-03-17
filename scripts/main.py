from globals import *


class App:
    def __init__(self, caption: str = '', icon: pygame.Surface = None) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(caption)
        if icon: pygame.display.set_icon(icon)
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
    game = App(caption='Game Jam', icon=pygame.image.load('..\\data\\amongus.png'))
    game.run()
