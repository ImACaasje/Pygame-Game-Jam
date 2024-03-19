from globals import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, pos: tuple, groups):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(center=pos)

