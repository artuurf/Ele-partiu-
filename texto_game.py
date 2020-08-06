import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.color = (0, 0, 0)
        self.texto = 0
        self.timeScore = 0
        self.font = pygame.font.Font("Facile Sans.otf", 20)
        self.image = self.font.render(str(self.texto), 1, self.color)
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.texto = f'Score: {int(self.timeScore)}M'
        self.image = self.font.render(str(self.texto), 1, self.color)

