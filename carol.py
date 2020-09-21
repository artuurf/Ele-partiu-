

import pygame
import math


class Carol(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/carol.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/carol1.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/carol.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/image/carol2.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [70, 80])
        self.sprite2 = pygame.transform.scale(self.sprite2, [70, 80])
        self.sprite3 = pygame.transform.scale(self.sprite3, [70, 80])
        self.sprite4 = pygame.transform.scale(self.sprite4, [70, 80])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/image/carol.png")
        self.image = pygame.transform.scale(self.image, [70, 80])
        self.rect = pygame.Rect(-100, 350, 70, 80)
        self.mask = pygame.mask.from_surface(self.image)

        self.timer = 0
        self.active = False
        self.active1 = False

    def update(self, *args):
        self.current_image = (self.current_image + 1) % 4
        self.image = self.images[self.current_image]
        if self.active:
            self.rect.x += 3
            if self.rect.x == 50 and self.active:
                self.active = False
                self.active1 = True
        elif self.active1:
            self.timer -= 0.1
            self.rect.x = 100 + math.sin(self.timer) * 120
        elif not self.active:
            self.rect = pygame.Rect(-100, 350, 70, 80)
            self.active1 = False


