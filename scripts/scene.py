from globals import *
from sprites import Sprite, MovingSprite


class Scene:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()

        self.textures = self.setup()

        # test
        self.note = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 10), (200, 200), self.all_sprites)
        self.note2 = MovingSprite(pygame.transform.scale_by(self.textures['note1vleugel'], 10), (200, 300), self.all_sprites)
        self.note3 = MovingSprite(pygame.transform.scale_by(self.textures['note2'], 10), (200, 100), self.all_sprites)
        self.note4 = MovingSprite(pygame.transform.scale_by(self.textures['note3'], 10), (200, 400), self.all_sprites)
        self.gsleutel = Sprite(pygame.transform.scale_by(self.textures['g-sleutel'], 10), (150, 200), self.all_sprites)

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
