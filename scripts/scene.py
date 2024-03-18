from globals import *
from sprites import Sprite, MovingSprite


class Scene:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()

        self.textures = self.setup()

        # test
        self.gsleutel = Sprite(pygame.transform.scale_by(self.textures['g-sleutel'], 10), (40, 200), self.all_sprites)
        self.tube1 = Sprite(pygame.transform.scale_by(self.textures['tubeVert'], 5), (450, 360), self.all_sprites)
        self.tube2 = Sprite(pygame.transform.scale_by(self.textures['tubeVert'], 5), (525, 360), self.all_sprites)
        self.tube3 = Sprite(pygame.transform.scale_by(self.textures['tubeVert'], 5), (600, 360), self.all_sprites)
        self.tube4 = Sprite(pygame.transform.scale_by(self.textures['tubeVert'], 5), (675, 360), self.all_sprites)
        self.tube5 = Sprite(pygame.transform.scale_by(self.textures['tubeVert'], 5), (750, 360), self.all_sprites)
        self.note1 = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 7), (self.tube1.rect.centerx, self.tube1.rect.centery), self.all_sprites)
        self.note2 = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 7),(self.tube2.rect.centerx, self.tube2.rect.centery), self.all_sprites)
        self.note3 = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 7),(self.tube3.rect.centerx, self.tube3.rect.centery), self.all_sprites)
        self.note4 = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 7),(self.tube4.rect.centerx, self.tube1.rect.centery), self.all_sprites)
        self.note5 = MovingSprite(pygame.transform.scale_by(self.textures['note1'], 7),(self.tube5.rect.centerx, self.tube1.rect.centery), self.all_sprites)

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
