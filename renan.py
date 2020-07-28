"""
self.speed = 5
"""


import pygame
import math


class Renan(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/image/renan.png")
        self.image = pygame.transform.scale(self.image, [110, 110])
        self.rect = pygame.Rect(860, 350, 110, 110)

        self.timer = 0

    def update(self, *args):
        self.timer -= 0.01

        self.rect.x = 700 + math.sin(self.timer) * 100
