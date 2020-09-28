import pygame


class Buzina(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.sprite1 = pygame.image.load("data/buzina.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/buzina1.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/buzina2.png").convert_alpha()

        self.sprite1 = pygame.transform.scale(self.sprite1, [180, 120])
        self.sprite2 = pygame.transform.scale(self.sprite2, [180, 120])
        self.sprite3 = pygame.transform.scale(self.sprite3, [180, 120])

        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       ]
        self.image = pygame.image.load("data/buzina.png")
        self.image = pygame.transform.scale(self.image, [180, 120])
        self.rect = pygame.Rect(860, 350, 860, 120)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0
        self.speed = 2
        self.active = False

    def update(self, *args):
        if self.active:
            # logica
            self.rect.x -= self.speed

            if self.rect.x == 380:
                self.image = self.images[2]
            elif self.rect.x == 385 or self.rect.x == 360:
                self.image = self.images[1]
            elif self.rect.x == 350:
                self.image = self.images[0]

            elif self.rect.right < 0:
                self.active = False
                self.rect.x = 860
