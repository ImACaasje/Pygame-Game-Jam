from globals import *
from tube import Tube


class Organ:
    def __init__(self, level):
        self.level = level
        self.screen = pygame.display.get_surface()

        self.keys_toggled = {'f': False,
                             'g': False,
                             'h': False,
                             'j': False,
                             'k': False}

        self.tubes = {"A": Tube('A'),
                 "B": Tube('B'),
                 "C": Tube('C'),
                 "D": Tube('D'),
                 "E": Tube('E'),
                 "F": Tube('F'),
                 "G": Tube('G')}

        self.rects = []

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            if not self.keys_toggled['f']:
                print('f pressed')
                self.keys_toggled['f'] = True
                self.tubes['A'].play_note()

        else:
            self.keys_toggled['f'] = False

        if keys[pygame.K_g]:
            if not self.keys_toggled['g']:
                print('g pressed')
                self.keys_toggled['g'] = True
                self.tubes['B'].play_note()
        else:
            self.keys_toggled['g'] = False

        if keys[pygame.K_h]:
            if not self.keys_toggled['h']:
                print('h pressed')
                self.keys_toggled['h'] = True
                self.tubes['C'].play_note()
        else:
            self.keys_toggled['h'] = False

        if keys[pygame.K_j]:
            if not self.keys_toggled['j']:
                print('j pressed')
                self.keys_toggled['j'] = True
                self.tubes['D'].play_note()
        else:
            self.keys_toggled['j'] = False

        if keys[pygame.K_k]:
            if not self.keys_toggled['k']:
                print('k pressed')
                self.keys_toggled['k'] = True
                self.tubes['E'].play_note()
        else:
            self.keys_toggled['k'] = False

    def update(self):
        self.input()
