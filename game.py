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
# pygame.mixer_music.load("data/audio/battleThemeA.mp3")
# pygame.mixer_music.play(-1)
jump = pygame.mixer.Sound("data/audio/jump.wav")
hit = pygame.mixer.Sound("data/audio/weird_16.ogg")
end = pygame.mixer.Sound("data/audio/GameOver.wav")
speed = 7
jumpCount = 10

gameLoop = False
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
keys = pygame.key.get_pressed()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


menu = True
click = False

if __name__ == "__main__":

    def main_menu():
        global menu, click, keys
        while menu:
            clock.tick(60)
            display.fill([170, 170, 170])
            draw_text('Leo Adventure', font, (0, 0, 0), display, 50, 40)

            mx, my = pygame.mouse.get_pos()

            # Definindo imagens do botão
            # __Botão 1__
            img1_button_1 = pygame.image.load("data/image/btn_play.png").convert_alpha()
            img2_button_1 = pygame.image.load("data/image/btn_play2.png").convert_alpha()
            # __Botão 2__
            img1_button_2 = pygame.image.load("data/image/btn_quit.png").convert_alpha()
            img2_button_2 = pygame.image.load("data/image/btn_quit2.png").convert_alpha()
            #imagem leo
            leonardo = pygame.image.load("data/image/leo_reality.png").convert_alpha()

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
                    return intro()

            # Efeito do botão Quit
            if button_2.collidepoint(mx, my):
                img1_button_2 = img2_button_2
                if click:
                    return pygame.quit()

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
        pygame.quit()

    def intro():
        pygame.mixer_music.load("data/audio/battleThemeA.mp3")
        pygame.mixer_music.play(-1)
        global gameover, game
        introduction = True
        while introduction:
            clock.tick(0)
            display.fill([0, 0, 0])
            draw_text('Era uma vez, um estagiário que conheceu um rapaz...', font, (255, 255, 255), display, 40, 40)
            draw_text('Ele não conhecia a fruta, mas mesmo assim experimentou...', font, (255, 255, 255), display, 40, 80)
            draw_text('Certo dia o rapaz teve que ir embora...', font, (255, 255, 255), display, 40, 120)
            draw_text('Então a bixa gladiadora foi atrás...', font, (255, 255, 255), display, 40, 160)

            draw_text('PRESSIONE ESPAÇO', font, (255, 255, 255), display, 40, 400)

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                #print(event.type)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        introduction = False
                        return game()

            pygame.display.update()
        pygame.quit()

    def game():
        # Objects
        objectGroup = pygame.sprite.Group()
        DelayGroup = pygame.sprite.Group()
        melGroup = pygame.sprite.Group()
        bugerGroup = pygame.sprite.Group()
        carolGroup = pygame.sprite.Group()

        # Fundo
        backgroud = PlanoFundo(objectGroup)
        newbackgroud = PlanoFundo(objectGroup)
        newbackgroud.rect.center = [430, 290]

        # Plataforma
        plataforma = Plataforma(objectGroup)
        newplataforma = Plataforma(objectGroup)
        newplataforma.rect.center = [430, 520]

        # buzina
        buz = Buzina(objectGroup)
        buz.rect.bottom = plataforma.rect.top
        buger = Buger(DelayGroup, bugerGroup)

        # Personagens
        leo = Leo(DelayGroup)
        leo.rect.bottom = plataforma.rect.top

        renan = Renan(DelayGroup)
        renan.rect.bottom = plataforma.rect.top

        carol = Carol(DelayGroup, carolGroup)
        carol.rect.bottom = plataforma.rect.top

        # texto

        text = Text(objectGroup)
        text.rect.center = [700, 50]

        text1 = Text(objectGroup)
        text1.rect.center = [50, 50]
        text1.selector = 2

        disco = Disco(DelayGroup)

        balao1 = Balao(objectGroup)
        balao1.image = balao1.images[1]

        balao = Balao(objectGroup)

        armario = Armario(objectGroup)

        global gameLoop, speed, gameover, jumpCount, timer, keys
        gameLoop = True
        frameDeTroca = 0
        timer = 0
        while gameLoop:
            clock.tick(60)
            text.timeScore += 0.01
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

            # Update Logic:
            frameAtual = pygame.time.get_ticks()

            timer += 1
            if random.random() < 0.6 and text.timeScore < 100 and not gameover and timer > 110:
                mel = Mel(DelayGroup, melGroup)
                mel.rect.center = renan.rect.center
                renan.image = renan.images[4]
                hit.play()
                timer = 0
            elif random.random() < 0.7 and text.timeScore >= 100 and not gameover and timer > 90:
                mel = Mel(DelayGroup, melGroup)
                mel.rect.center = renan.rect.center
                hit.play()
                timer = 0

            if buz.rect.x == 320:
                buger.arremessar = True
                buger.rect.x = 350

            colisao = pygame.sprite.spritecollide(leo, melGroup, False)
            life = pygame.sprite.spritecollide(leo, bugerGroup, False)
            carolpego = pygame.sprite.spritecollide(leo, carolGroup, False)

            if colisao:
                tomou = pygame.sprite.groupcollide(melGroup, objectGroup, True, False)
                leo.image = leo.images[4]
                text1.life -= 1
                if text1.life < 0:
                    text.timeScore = 0
                    text1.life = 0
                    gameover = True
                    pygame.mixer_music.stop()
                    end.play()

            elif life:
                tomou = pygame.sprite.groupcollide(bugerGroup, objectGroup, True, False)
                text1.life += 1

            elif carolpego:
                tomou = pygame.sprite.groupcollide(carolGroup, objectGroup, False, False)
                text1.life -= 1
                if text1.life < 0:
                    text.timeScore = 0
                    text1.life = 0
                    gameover = True
                    pygame.mixer_music.stop()
                    end.play()

            if frameAtual > frameDeTroca:
                frameDeTroca += 150
                DelayGroup.update()
                if int(text.timeScore) == 30:
                    buz.active = True
                elif int(text.timeScore) == 80:
                    buz.active = True
                elif int(text.timeScore) == 50:
                    carol.active = True
                elif int(text.timeScore) == 54:
                    balao.rect.left = carol.rect.right + 10
                    balao.active = True

                elif int(text.timeScore) == 15:
                    balao1.active = True
                    balao1.rect.right = renan.rect.left - 10

                elif int(text.timeScore) == 40:
                    disco.active = True

            elif not gameover:
                objectGroup.update()
                # Draw:
                display.fill([19, 173, 235])
                objectGroup.draw(display)
                DelayGroup.draw(display)
                pygame.display.update()

        pygame.quit()

    main_menu()
