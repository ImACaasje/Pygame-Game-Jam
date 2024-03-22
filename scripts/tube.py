import pygame


class Tube:
    def __init__(self, tone, screen, x, y):
        self.tube_image = pygame.transform.scale_by(
            pygame.image.load('..\\data\\sprites\\tubes\\tubeVert.png'), 5)
        self.tube_rect = self.tube_image.get_rect()
        self.tube_rect.center = (x, y)
        self.tone = tone
        self.screen = screen
        self.x = x
        self.y = y

    def draw_tube(self, state):
        """Draw Tube on screen"""
        if state == 'inactive':
            self.screen.blit(self.tube_image, self.tube_rect)

        print('draw')

    def play_note(self):
        path_to_note = f'..\\data\\soundeffects\\notes\\note_{self.tone}.wav'
        note_sound = pygame.mixer.Sound(path_to_note)
        note_sound.play()