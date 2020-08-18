

import pygame
import math


class Balao(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/balaoviado.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/balaorenan.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/balaorodrigo.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [130, 90])
        self.sprite2 = pygame.transform.scale(self.sprite2, [130, 90])
        self.sprite3 = pygame.transform.scale(self.sprite3, [130, 90])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3
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

