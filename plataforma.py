import pygame


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/image/ground.png")
        self.image = pygame.transform.scale(self.image, [865, 180])
        self.rect = self.image.get_rect()
        self.rect.center = [430, 520]

        self.speed = 5
        self.rect.x = 860

    def update(self, *args):
        # logica
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.rect.left = 860

