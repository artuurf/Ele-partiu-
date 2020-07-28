"""
# Apertar W e soltar

elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        isPressingW = True
                        print('Apertou W!')
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        isPressingW = False
                        print('Soltouuu')

# Criar um retangulo com o posicionamento e tamanho
retangulo = pygame.Reck(50, 50, 100, 100) # x, y, w, h

# Definindo a cor do retangulo
pygame.draw.rect(display, [255, 255, 255, 255], retangulo)
"""

import pygame
from leo import Leo
from renan import Renan
from backgroud import PlanoFundo
from plataforma import Plataforma

# Inicializando o pygame e criando a Janela
pygame.init()

largura = 860
altura = 580
timer = 0

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ele partiu!")

# Objects
objectGroup = pygame.sprite.Group()

# Background
backgroud = PlanoFundo(objectGroup)
newbackgroud = PlanoFundo(objectGroup)
newbackgroud.rect.center = [430, 290]


# Plataforma
plataforma = Plataforma(objectGroup)
newplataforma = Plataforma(objectGroup)
newplataforma.rect.center = [430, 520]

leo = Leo(objectGroup)
leo.rect.center = [300, 380]

renan = Renan(objectGroup)

# Music
# pygame.mixer_music.load("data/score.mp3")
# pygame.mixer_music.play(-1)


gameLoop = True
clock = pygame.time.Clock()
isPressingW = False
key = pygame.key.get_pressed()


if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False





            """elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    leo.rect.y -= 40
                    if leo.rect.bottom >= 420:
                        leo.rect.bottom = plataforma.rect.top
                        print('chega irmão')

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # leo.rect.bottom = plataforma.rect.top
                    print('Soltou')"""


        # Update Logic:
        objectGroup.update()

        # Draw:

        display.fill([19, 173, 235])
        objectGroup.draw(display)
        pygame.display.update()


