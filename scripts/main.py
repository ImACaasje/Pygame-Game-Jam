from globals import *
from scene import Scene
from organ import Organ


class App:
    def __init__(self, caption: str = '', icon: pygame.Surface = None) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption(caption)
        if icon: pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()

        self.Scene = Scene()
        self.Organ = Organ(1)

    def run(self) -> None:
        while True:
            dt = self.clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()

            self.Organ.update()
            self.Scene.update(dt)
            pygame.display.update()

    def close(self) -> None:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = App(caption='Tubes Of Melody', icon=pygame.image.load('..\\data\\sprites\\notes\\note1vleugel.png'))
    game.run()
