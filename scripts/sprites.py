from globals import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, pos: tuple, groups):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(topleft=pos)


class MovingSprite(Sprite):  # dis bullshit eigenlijk maar ik wou ff uittesten
    def __init__(self, img: pygame.Surface, pos: tuple, groups):
        super().__init__(img, pos, groups)
        self.dir = Vector()
        self.dir.x = 1

    def update(self, dt):
        self.rect.x += self.dir.x
        if self.rect.x >= SCREENWIDTH:
            self.dir.x = -1
        if self.rect.x <= 0:
            self.dir.x = 1
