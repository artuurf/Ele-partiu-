import pygame


class Buger(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/image/buger.png")
        self.image = pygame.transform.scale(self.image, [35, 35])
        self.rect = pygame.Rect(300, 360, 35, 35)
        self.mask = pygame.mask.from_surface(self.image)
        self.arremessar = True
        self.speed = 5
        self.count = 9

    def update(self, *args):
        if self.arremessar:
            self.rect.x -= self.speed
            self.rect.y -= (self.count * abs(self.count)) * 0.5
            self.count -= 1
