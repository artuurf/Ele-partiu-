import pygame
import math


class PlanoFundo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/image/imagefundo.png")
        self.image = pygame.transform.scale(self.image, [860, 580])
        self.rect = pygame.Rect(0, 0, 860, 580)

        self.rect.x = 860

        self.speed = 4

    def update(self, *args):
        # logica
        self.rect.x -= self.speed

        if self.rect.right == 0:
            self.rect.left = 860



"""
# Background

        self.image = pygame.image.load("data/image/imagefundo.png")
        self.image = pygame.transform.scale(self.image, [860, 580])
        self.rect = self.image.get_rect()
        
                if self.rect.right == 0:
            print('mata')
            self.kill()
"""
