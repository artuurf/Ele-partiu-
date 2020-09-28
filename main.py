import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame
from leo import Leo
from renan import Renan
from backgroud import PlanoFundo
from plataforma import Plataforma
from mel import Mel
import random
import pygame.freetype
from texto_game import Text
from buzina import Buzina
from buger import Buger
from pygame.locals import *
from carol import Carol
from text_balao import Balao
from disco import Disco
from armario import Armario
from rodrigo import Rodrigo

# Inicializando o pygame e criando a Janela
pygame.init()

largura = 860
altura = 580
gameover = False
game = False
introduction = False

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Leo Adventure")

# Music

jump = pygame.mixer.Sound("data/jump.wav")
hit = pygame.mixer.Sound("data/weird_16.wav")
end = pygame.mixer.Sound("data/GameOver.wav")
lifeBuzina = pygame.mixer.Sound("data/score.wav")
speed = 7
jumpCount = 10

gameLoop = False
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
keys = pygame.key.get_pressed()



# Objects
objectGroup = pygame.sprite.Group()
DelayGroup = pygame.sprite.Group()
melGroup = pygame.sprite.Group()
bugerGroup = pygame.sprite.Group()
carolGroup = pygame.sprite.Group()
rodrigoGroup = pygame.sprite.Group()

# Fundo
backgroud = PlanoFundo(objectGroup)
newbackgroud = PlanoFundo(objectGroup)
newbackgroud.rect.center = [430, 290]

backgroud1 = PlanoFundo(objectGroup)
newbackgroud1 = PlanoFundo(objectGroup)
newbackgroud1.rect.center = [430, 290]
backgroud1.image = backgroud1.images[1]
newbackgroud1.image = newbackgroud1.images[1]
backgroud1.speed = 1
newbackgroud1.speed = 1

backgroud2 = PlanoFundo(objectGroup)
backgroud2.image = backgroud2.images[2]
newbackgroud2 = PlanoFundo(objectGroup)
newbackgroud2.rect.center = [430, 290]
newbackgroud2.image = newbackgroud2.images[2]
backgroud2.speed = 2
newbackgroud2.speed = 2

backgroud3 = PlanoFundo(objectGroup)
newbackgroud3 = PlanoFundo(objectGroup)
newbackgroud3.rect.center = [430, 290]
backgroud3.image = backgroud3.images[3]
newbackgroud3.image = newbackgroud2.images[3]
backgroud3.speed = 3
newbackgroud3.speed = 3

# Plataforma
plataforma = Plataforma(objectGroup)
newplataforma = Plataforma(objectGroup)
newplataforma.rect.center = [430, 520]

# buzina
buz = Buzina(objectGroup)
buz.rect.bottom = plataforma.rect.top

# Personagens
leo = Leo(DelayGroup)
leo.rect.bottom = plataforma.rect.top

renan = Renan(DelayGroup)
renan.rect.bottom = plataforma.rect.top

carol = Carol(DelayGroup, carolGroup)
carol.rect.bottom = plataforma.rect.top

nasci = Rodrigo(objectGroup)
nasci.rect.bottom = plataforma.rect.top
nasci.image = nasci.images[2]
nasci.rect.y = 340

# texto

text = Text(objectGroup)
text.rect.center = [700, 50]

text1 = Text(objectGroup)
text1.rect.center = [50, 50]
text1.selector = 2

# Balao Renan
balao1 = Balao(objectGroup)
balao1.image = balao1.images[1]

# balao Carol
balao = Balao(objectGroup)

# Balao Rodrigo
balao2 = Balao(objectGroup)
balao2.image = balao2.images[2]

# Balao Nasci
balao3 = Balao(objectGroup)
balao3.image = balao3.images[3]

rodrigo = Rodrigo(objectGroup, rodrigoGroup)
disco = Disco(DelayGroup)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

menu = True
introduction = True
click = False
gameover_end = False
game_end = False

if __name__ == "__main__":

    gameLoop = True
    timer = 0
    while gameLoop:

        clock.tick(60)
        text.timeScore += 0.01

        # -------------------------------------------- // --------------------------------------------
        # Definindo menu
        while menu:
            clock.tick(60)
            display.fill([170, 170, 170])
            #draw_text('Leo Adventure', font, (0, 0, 0), display, 50, 40)

            mx, my = pygame.mouse.get_pos()

            # Definindo imagens do botão
            # __Botão 1__
            img1_button_1 = pygame.image.load("data/btn_play.png").convert_alpha()
            img2_button_1 = pygame.image.load("data/btn_play2.png").convert_alpha()
            # __Botão 2__
            img1_button_2 = pygame.image.load("data/btn_quit.png").convert_alpha()
            img2_button_2 = pygame.image.load("data/btn_quit2.png").convert_alpha()
            #imagem leo
            leonardo = pygame.image.load("data/leo_reality.png").convert_alpha()

            # Ajustando tamanho do botão
            # __Botão 1__
            img1_button_1 = pygame.transform.scale(img1_button_1, [200, 50])
            img2_button_1 = pygame.transform.scale(img2_button_1, [200, 50])
            # __Botão 2__
            img1_button_2 = pygame.transform.scale(img1_button_2, [200, 50])
            img2_button_2 = pygame.transform.scale(img2_button_2, [200, 50])

            # Imagem leo
            leonardo = pygame.transform.scale(leonardo, [420, 300])

            # Botão invisivel para clique
            button_1 = pygame.Rect(170, 400, 200, 50)
            button_2 = pygame.Rect(470, 400, 200, 50)

            # Efeito do botão Play
            if button_1.collidepoint(mx, my):
                img1_button_1 = img2_button_1
                if click:
                    pygame.mixer_music.load("data/battleThemeA.mp3")
                    pygame.mixer_music.play(-1)
                    menu = False

            # Efeito do botão Quit
            if button_2.collidepoint(mx, my):
                img1_button_2 = img2_button_2
                if click:
                    pygame.quit()

            # Inserindo botões no menu
            display.blit(img1_button_1, (170, 400))
            display.blit(img1_button_2, (470, 400))
            display.blit(leonardo, (250, 70))

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

        # -------------------------------------------- // --------------------------------------------
        # Definindo Introdução
        while introduction:
            clock.tick(60)
            display.fill([0, 0, 0])
            draw_text('Ajude o Leo a alcançar o amor da sua vida!', font, (255, 255, 255), display, 40, 40)
            draw_text('REGRAS:', font, (255, 255, 255), display, 40, 80)
            draw_text('Desvie de todos os mel;', font, (255, 255, 255), display, 40, 120)
            draw_text('Pegue o maximo de buzinas possiveis;', font, (255, 255, 255), display, 40, 160)
            draw_text('Não deixe o Rodrigo pegar seus buzinas;', font, (255, 255, 255), display, 40, 200)
            draw_text('Ao chegar aos 100M, não deixe o Boss te pegar mesmo se tiver buzinas;', font, (255, 255, 255), display, 40, 240)

            draw_text('PRESSIONE ESPAÇO', font, (255, 255, 255), display, 40, 400)

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        frameDeTroca = pygame.time.get_ticks()
                        introduction = False
                        armario = Armario(objectGroup)
                        leo.rect.x = 100
                        text1.life = 1

            pygame.display.update()

        # -------------------------------------------- // --------------------------------------------
        # Game Over
        while gameover_end:
            carol.active = False
            clock.tick(60)
            display.fill([0, 0, 0])
            nao_deu = pygame.image.load("data/nao_deu.png").convert_alpha()
            nao_deu = pygame.transform.scale(nao_deu, [300, 80])
            leo_nao_deu = pygame.image.load("data/Leo_mel.png").convert_alpha()
            leo_nao_deu = pygame.transform.scale(leo_nao_deu, [90, 90])

            draw_text('PRESSIONE ESPAÇO PARA TENTAR NOVAMENTE', font, (255, 255, 255), display, 170, 450)

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        introduction = True
                        menu = True
                        gameover_end = False
                        gameover = False
                        carol.right = 0
                        buz.right = 0
                        rodrigo.right = 0
                        # pygame.mixer_music.load("data/battleThemeA.mp3")
                        # pygame.mixer_music.play(-1)

            display.blit(nao_deu, (300, 100))
            display.blit(leo_nao_deu, (400, 250))

            pygame.display.update()

        # -------------------------------------------- // --------------------------------------------
        # fim
        while game_end:
            pygame.mixer_music.stop()
            carol.active = False
            clock.tick(60)
            display.fill([0, 0, 0])
            agora_deu = pygame.image.load("data/fim.png").convert_alpha()
            agora_deu = pygame.transform.scale(agora_deu, [800, 400])


            # creditos = pygame.image.load("data/image/creditos.png").convert_alpha()
            # creditos = pygame.transform.scale(creditos, [800, 900])

            draw_text('Homenagem ao Leonardo, e sua linda história de amor', font, (255, 255, 255), display, 100, 400)
            draw_text('Autor, desenvolvedor e designer: Artur Filipe', font, (255, 255, 255), display, 150, 460)
            draw_text('Participação importante no desenvolvimento: Felipe Maeda', font, (255, 255, 255), display, 150, 500)
            draw_text('Audio: opengameart.org', font, (255, 255, 255), display, 150, 540)

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        introduction = True
                        menu = True
                        gameover_end = False
                        gameover = False
                        game_end = False

            creditos = Balao(objectGroup)
            #creditos.image = creditos.images[4]
            creditos.rect.center = [300, 300]

                        # pygame.mixer_music.load("data/audio/battleThemeA.mp3")
                        # pygame.mixer_music.play(-1)

            # display.blit(creditos, (100, 400))
            display.blit(agora_deu, (0, 0))

            pygame.display.update()

        # Definindo colisão
        colisao = pygame.sprite.spritecollide(leo, melGroup, False)
        life = pygame.sprite.spritecollide(leo, bugerGroup, False)
        carolpego = pygame.sprite.spritecollide(leo, carolGroup, False)
        roubobuzina = pygame.sprite.spritecollide(leo, rodrigoGroup, False, pygame.sprite.collide_mask)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        keys = pygame.key.get_pressed()
        # Movimentação horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and leo.rect.x > speed:
            leo.speed -= 0.1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and leo.rect.x < 500 - speed - 100:
            leo.speed += 0.1

        else:
            leo.speed *= 0.98

        leo.rect.x += leo.speed

        if not leo.isJump:

            if keys[pygame.K_SPACE] and not gameover:
                jump.play()
                leo.isJump = True
        else:
            if jumpCount >= -9:
                leo.rect.y -= (jumpCount * abs(jumpCount)) * 0.1
                jumpCount -= 0.3

            else:
                jumpCount = 9
                leo.isJump = False
                leo.rect.bottom = plataforma.rect.top

        timer += 1
        if random.random() < 0.6 and text.timeScore < 130 and not gameover and timer > 130:
            mel = Mel(DelayGroup, melGroup)
            mel.rect.center = renan.rect.center
            renan.image = renan.images[4]
            hit.play()
            timer = 0
        elif random.random() < 0.7 and text.timeScore >= 130 and not gameover and timer > 90:
            mel = Mel(DelayGroup, melGroup)
            mel.rect.center = renan.rect.center
            hit.play()
            timer = 0

        if buz.rect.x == 380:
            buger = Buger(objectGroup, bugerGroup)
            buger.arremessar = True
            buger.rect.x = 381

        if colisao:
            tomou = pygame.sprite.groupcollide(melGroup, objectGroup, True, False)
            leo.image = leo.images[4]
            text1.life -= 1
            if text1.life < 0:
                text.timeScore = 0
                text1.life = 0
                gameover = True
                gameover_end = True
                pygame.mixer_music.stop()
                end.play()

        elif life:
            tomou = pygame.sprite.groupcollide(bugerGroup, objectGroup, True, False)
            text1.life += 1
            lifeBuzina.play()

        elif carolpego:
            tomou = pygame.sprite.groupcollide(carolGroup, objectGroup, False, False)
            text1.life -= 1
            if text1.life < 0:
                text.timeScore = 0
                text1.life = 0
                gameover = True
                gameover_end = True
                pygame.mixer_music.stop()
                end.play()

        elif roubobuzina and text1.life > 0:
            rodrigo.image = rodrigo.images[1]
            text1.life -= 1

        # Update Logic:
        frameAtual = pygame.time.get_ticks()
        if frameAtual > frameDeTroca:
            frameDeTroca += 150
            DelayGroup.update()
            # Momento para personagens aparecerem
            if int(text.timeScore) == 15:
                buz.active = True
            elif int(text.timeScore) == 40:
                buz.active = True
            elif int(text.timeScore) == 70:
                buz.active = True
            elif int(text.timeScore) == 120:
                buz.active = True
            elif int(text.timeScore) == 100:
                carol.active = True
            elif int(text.timeScore) == 102:
                balao.rect.left = carol.rect.right + 10
                balao.active = True
            elif int(text.timeScore) == 9:
                balao1.active = True
                balao1.rect.right = renan.rect.left - 10
            elif int(text.timeScore) == 30:
                disco.active = True
            elif int(text.timeScore) == 25:
                rodrigo.active = True
            elif int(text.timeScore) == 26:
                balao2.active = True
                balao2.rect.right = rodrigo.rect.left
            elif int(text.timeScore) == 50:
                rodrigo.active = True
            elif int(text.timeScore) == 80:
                rodrigo.active = True
            elif int(text.timeScore) == 51:
                balao2.active = True
                balao2.rect.right = rodrigo.rect.left
            elif int(text.timeScore) == 60:
                nasci.active = True
            elif int(text.timeScore) == 62:
                nasci.image = nasci.images[3]
                balao3.active = True
                balao3.rect.right = nasci.rect.left
            elif int(text.timeScore) == 200:
                game_end = True

        objectGroup.draw(display)
        DelayGroup.draw(display)
        objectGroup.update()
        pygame.display.update()

    pygame.quit()




