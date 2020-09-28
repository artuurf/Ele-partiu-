import pygame


class Buger(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/buger.png")
        self.image = pygame.transform.scale(self.image, [45, 35])
        self.rect = pygame.Rect(900, 360, 45, 35)
        self.mask = pygame.mask.from_surface(self.image)
        self.arremessar = False
        self.speed = 2
        self.count = 11

    def update(self, *args):
        if self.arremessar:
            self.rect.x -= self.speed
            self.rect.y -= (self.count * abs(self.count)) * 0.1
            self.count -= 0.2
            if self.rect.y > 580:
                self.rect.y = 900
                self.arremessar = False
