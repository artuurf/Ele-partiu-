

import pygame
import math


class Disco(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/disco.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/disco1.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [120, 40])
        self.sprite2 = pygame.transform.scale(self.sprite2, [120, 40])

        self.images = [self.sprite1,
                       self.sprite2
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/disco.png")
        self.image = pygame.transform.scale(self.image, [120, 40])
        self.rect = pygame.Rect(860, 350, 120, 40)
        self.mask = pygame.mask.from_surface(self.image)
        self.active = False
        self.timer = 0

    def update(self, *args):
        if self.active:
            self.timer -= 0.1
            self.rect.y = 100 + math.sin(self.timer) * 30
            self.rect.x -= 10
            self.current_image = (self.current_image + 1) % 2
            self.image = self.images[self.current_image]
            if self.rect.right < 0:
                self.kill()
