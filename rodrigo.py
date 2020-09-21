

import pygame


class Rodrigo(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/image/rodrigo.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/rodrigo_buger.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/nasci.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/image/nasci1.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [70, 80])
        self.sprite2 = pygame.transform.scale(self.sprite2, [90, 80])
        self.sprite3 = pygame.transform.scale(self.sprite3, [75, 90])
        self.sprite4 = pygame.transform.scale(self.sprite4, [75, 90])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4
                       ]

        self.current_image = 0

        self.image = pygame.image.load("data/image/rodrigo.png")
        self.image = pygame.transform.scale(self.image, [70, 80])
        self.rect = pygame.Rect(860, 350, 70, 80)
        self.mask = pygame.mask.from_surface(self.image)
        self.active = False

    def update(self, *args):
        if self.active:
            self.rect.x -= 2
            if self.rect.right < 0 and self.image == self.images[1]:
                self.active = False
                self.rect.x = 860
                self.image = self.images[0]
            elif self.rect.right < 0 and self.image == self.images[3]:
                self.active = False
                self.rect.x = 860
                self.image = self.images[2]




