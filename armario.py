

import pygame
import math


class Armario(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/armario.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/armario1.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [130, 140])
        self.sprite2 = pygame.transform.scale(self.sprite2, [130, 140])

        self.images = [self.sprite1,
                       self.sprite2
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/image/armario1.png")
        self.image = pygame.transform.scale(self.image, [130, 140])
        self.rect = pygame.Rect(100, 305, 130, 140)
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True
        self.timer = 0

    def update(self, *args):
        if self.active:
            self.rect.x -= 2
            if self.rect.right <= 0:
                self.kill()
