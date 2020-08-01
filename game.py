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

# Fundo
backgroud = PlanoFundo(objectGroup)
newbackgroud = PlanoFundo(objectGroup)
newbackgroud.rect.center = [430, 290]


# Plataforma
plataforma = Plataforma(objectGroup)
newplataforma = Plataforma(objectGroup)
newplataforma.rect.center = [430, 520]

# Personagens

leo = Leo(objectGroup)
leo.rect.bottom = plataforma.rect.top

renan = Renan(objectGroup)

# Music
# pygame.mixer_music.load("data/score.mp3")
# pygame.mixer_music.play(-1)
jump = pygame.mixer.Sound("data/audio/jump.wav")
timeScore = 0
speed = 4
jumpCount = 9
isJump = True
gameLoop = True
clock = pygame.time.Clock()

if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        print(leo.time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a] and leo.rect.x > speed:
            leo.rect.x -= speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and leo.rect.x < 500 - speed - 100:
            leo.rect.x += speed

        if not isJump:

            if keys[pygame.K_SPACE]:
                jump.play()
                isJump = True
        else:
            if jumpCount >= -9:
                leo.rect.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 9
                isJump = False
                leo.rect.bottom = plataforma.rect.top

        # Update Logic:
        objectGroup.update()

        # Draw:

        display.fill([19, 173, 235])
        objectGroup.draw(display)
        pygame.display.update()


