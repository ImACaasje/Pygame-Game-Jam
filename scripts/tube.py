import pygame


class Tube:
    def __init__(self, tone):
        self.tone = tone

    def play_note(self):
        path_to_note = f'..\\data\\soundeffects\\notes\\note_{self.tone}.wav'
        note_sound = pygame.mixer.Sound(path_to_note)
        note_sound.play()