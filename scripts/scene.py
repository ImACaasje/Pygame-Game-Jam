from globals import *
from sprites import Sprite


class Scene:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()

        self.textures = self.setup()

        # test
        self.gsleutel = Sprite(pygame.transform.scale_by(self.textures['g-sleutel'], 10), (40, 200), self.all_sprites)
        self.organ = Sprite(pygame.Surface((400, 300)), (SCREENWIDTH / 2, SCREENHEIGHT / 2), self.all_sprites)

    @staticmethod
    def setup() -> dict:
        textures = {}
        for name, path in SPRITES.items():
            textures[name] = pygame.image.load(path).convert_alpha()

        return textures

    def update(self, dt):
        self.screen.fill('lightblue')
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.screen)
