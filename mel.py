import pygame
import random


class Mel(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/mel.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/mel1.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/mel2.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/image/mel3.png").convert_alpha()
        self.sprite5 = pygame.image.load("data/image/mel4.png").convert_alpha()
        self.sprite6 = pygame.image.load("data/image/mel5.png").convert_alpha()
        self.sprite7 = pygame.image.load("data/image/mel6.png").convert_alpha()
        self.sprite8 = pygame.image.load("data/image/mel7.png").convert_alpha()
        self.sprite9 = pygame.image.load("data/image/mel_caido.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [30, 40])
        self.sprite2 = pygame.transform.scale(self.sprite2, [40, 50])
        self.sprite3 = pygame.transform.scale(self.sprite3, [40, 30])
        self.sprite4 = pygame.transform.scale(self.sprite4, [40, 40])
        self.sprite5 = pygame.transform.scale(self.sprite5, [30, 40])
        self.sprite6 = pygame.transform.scale(self.sprite6, [40, 50])
        self.sprite7 = pygame.transform.scale(self.sprite7, [40, 30])
        self.sprite8 = pygame.transform.scale(self.sprite8, [40, 40])
        self.sprite9 = pygame.transform.scale(self.sprite9, [50, 30])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4,
                       self.sprite5,
                       self.sprite6,
                       self.sprite7,
                       self.sprite8,
                       self.sprite9
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/image/mel.png")
        self.image = pygame.transform.scale(self.image, [30, 40])
        self.rect = pygame.Rect(700, 360, 30, 40)
        self.mask = pygame.mask.from_surface(self.image)
        self.arremessar = True
        self.speed = 30
        self.count = 9

    def update(self, *args):
        if self.arremessar:
            self.rect.x -= self.speed
            self.rect.y -= (self.count * abs(self.count)) * 0.5
            self.count -= 1
            if random.random() < 0.3:
                self.count -= 1
            elif random.random() > 0.7:
                self.count -= 5
            else:
                self.count += 1

            self.current_image = (self.current_image + 1) % 8
            self.image = self.images[self.current_image]
            if self.rect.right < 0:
                self.kill()
            elif self.rect.y > 400:
                self.rect.y = 400
                self.image = self.images[8]



