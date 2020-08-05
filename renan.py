"""
self.speed = 5
"""


import pygame
import math


class Renan(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/renan.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/Renan1.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/renan.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/image/Renan2.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [100, 100])
        self.sprite2 = pygame.transform.scale(self.sprite2, [100, 100])
        self.sprite3 = pygame.transform.scale(self.sprite3, [100, 100])
        self.sprite4 = pygame.transform.scale(self.sprite4, [100, 100])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/image/renan.png")
        self.image = pygame.transform.scale(self.image, [110, 110])
        self.rect = pygame.Rect(860, 350, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)

        self.timer = 0

    def update(self, *args):
        self.timer -= 0.1

        self.rect.x = 650 + math.sin(self.timer) * 100
        self.current_image = (self.current_image + 1) % 4
        self.image = self.images[self.current_image]
