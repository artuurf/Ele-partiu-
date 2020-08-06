
import pygame
from leo import Leo
from renan import Renan
from backgroud import PlanoFundo
from plataforma import Plataforma
from mel import Mel
import random
import pygame.freetype

# Inicializando o pygame e criando a Janela
pygame.init()

largura = 860
altura = 580
timer = 0

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ele partiu!")


# Objects
objectGroup = pygame.sprite.Group()
DelayGroup = pygame.sprite.Group()
melGroup = pygame.sprite.Group()

# Fundo
backgroud = PlanoFundo(objectGroup)
newbackgroud = PlanoFundo(objectGroup)
newbackgroud.rect.center = [430, 290]

# Plataforma
plataforma = Plataforma(objectGroup)
newplataforma = Plataforma(objectGroup)
newplataforma.rect.center = [430, 520]

# Personagens
leo = Leo(DelayGroup)
leo.rect.bottom = plataforma.rect.top

renan = Renan(DelayGroup)
renan.rect.bottom = plataforma.rect.top


# Music
# pygame.mixer_music.load("data/score.mp3")
# pygame.mixer_music.play(-1)
jump = pygame.mixer.Sound("data/audio/jump.wav")
timeScore = 0
speed = 7
jumpCount = 10
isJump = True
gameLoop = True
clock = pygame.time.Clock()
frameDeTroca = 0

GAME_FONT = pygame.freetype.Font("Facile Sans.otf", 20)


if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        # print(pygame.time.get_ticks())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        keys = pygame.key.get_pressed()

        # Movimentação horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and leo.rect.x > speed:
            leo.speed -= leo.acceleration

        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and leo.rect.x < 500 - speed - 100:
            leo.speed += leo.acceleration

        else:
            leo.speed *= 0.98

        leo.rect.x += leo.speed

        if not isJump:

            if keys[pygame.K_SPACE]:
                jump.play()
                isJump = True
        else:
            if jumpCount >= -9:
                leo.rect.y -= (jumpCount * abs(jumpCount)) * 0.1
                jumpCount -= 0.3
            else:
                jumpCount = 9
                isJump = False
                leo.rect.bottom = plataforma.rect.top

        # Update Logic:
        frameAtual = pygame.time.get_ticks()

        timer += 1
        if timer > 90:
            timer = 0
            if random.random() < 0.7:
                mel = Mel(DelayGroup, melGroup)
                mel.rect.center = renan.rect.center

        colisao = pygame.sprite.spritecollide(leo, melGroup, False)

        if colisao:
            tomou = pygame.sprite.groupcollide(melGroup, objectGroup, True, False)
            leo.image = leo.images[4]

        if frameAtual > frameDeTroca:
            frameDeTroca += 150
            timeScore += 0.17
            DelayGroup.update()

        GAME_FONT.render_to(display, (700, 30), f"Score: {int(timeScore)}M", (0, 0, 0))
        pygame.display.flip()

        objectGroup.update()

        # Draw:
        display.fill([19, 173, 235])
        objectGroup.draw(display)
        DelayGroup.draw(display)
        pygame.display.update()

    pygame.quit()

