from globals import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, pos: tuple, groups):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(center=pos)


class MovingSprite(Sprite):  # dis bullshit eigenlijk maar ik wou ff uittesten
    def __init__(self, img: pygame.Surface, pos: tuple, groups):
        super().__init__(img, pos, groups)
        self.dir = Vector()
        self.dir.y = 1
        self.pos = pos

    def update(self, dt):
        self.rect.y -= 1
        if self.rect.y < -140:
            self.rect.y = self.pos[1]
