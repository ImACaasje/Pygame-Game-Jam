from globals import *
from tube import Tube


class Organ:
    def __init__(self, level):
        self.level = level
        self.screen = pygame.display.get_surface()

        self.keys_toggled = {'F': False,
                             'G': False,
                             'H': False,
                             'J': False,
                             'K': False}

        self.tubes = {"F": Tube('A', self.screen, 400, 450),
                      "G": Tube('B', self.screen, 450, 450),
                      "H": Tube('C', self.screen, 500, 450),
                      "J": Tube('D', self.screen, 550, 450),
                      "K": Tube('E', self.screen, 600, 450)}

        self.rects = []

    def update_tubes(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            if not self.keys_toggled['F']:
                self.keys_toggled['F'] = True
                self.tubes['F'].play_note()

        else:
            self.keys_toggled['F'] = False

        if keys[pygame.K_g]:
            if not self.keys_toggled['G']:
                self.keys_toggled['G'] = True
                self.tubes['G'].play_note()
        else:
            self.keys_toggled['G'] = False

        if keys[pygame.K_h]:
            if not self.keys_toggled['H']:
                self.keys_toggled['H'] = True
                self.tubes['H'].play_note()
        else:
            self.keys_toggled['H'] = False

        if keys[pygame.K_j]:
            if not self.keys_toggled['J']:
                self.keys_toggled['J'] = True
                self.tubes['J'].play_note()
        else:
            self.keys_toggled['J'] = False

        if keys[pygame.K_k]:
            if not self.keys_toggled['K']:
                self.keys_toggled['K'] = True
                self.tubes['K '].play_note()
        else:
            self.keys_toggled['K'] = False

        # // update all tubes
        for tube_name, tube in self.tubes.items():
            if self.keys_toggled[tube_name] is False:
                state = 'inactive'
            else:
                state = 'active'

            tube.draw_tube(state)


