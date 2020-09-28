

import pygame


class Balao(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/balaoviado.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/balaorenan.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/balaorodrigo.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/balaonasci.png").convert_alpha()


        self.sprite1 = pygame.transform.scale(self.sprite1, [130, 90])
        self.sprite2 = pygame.transform.scale(self.sprite2, [130, 90])
        self.sprite3 = pygame.transform.scale(self.sprite3, [130, 90])
        self.sprite4 = pygame.transform.scale(self.sprite4, [130, 90])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4
                       ]

        self.rect = pygame.Rect(-150, 250, 130, 90)
        self.timer = 0
        self.active = False
        self.image = self.images[0]

    def update(self, *args):
        if self.active:
            self.timer += 0.1
            if self.timer >= int(18):
                self.kill()
                self.active = False
            elif self.image == self.images[3] or self.image == self.images[2]:
                self.rect.x -= 2


