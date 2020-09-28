import pygame


class PlanoFundo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprite1 = pygame.image.load("data/cidade.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/cidade1.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/cidade2.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/cidade3.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [1200, 580])
        self.sprite2 = pygame.transform.scale(self.sprite2, [1200, 580])
        self.sprite3 = pygame.transform.scale(self.sprite3, [1200, 580])
        self.sprite4 = pygame.transform.scale(self.sprite4, [1200, 580])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4
                       ]

        self.image = pygame.image.load("data/cidade.png")
        self.image = pygame.transform.scale(self.image, [1200, 580])
        self.rect = pygame.Rect(0, 0, 1200, 580)
        self.mask = pygame.mask.from_surface(self.image)
        self.active = False

        self.rect.x = 1030

        self.speed = 0

    def update(self, *args):
        # logica
        self.rect.x -= self.speed

        if self.rect.right <= 0:
            self.rect.left = 1200


