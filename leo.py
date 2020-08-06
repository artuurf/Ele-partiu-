import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

GROUND_WIDTH = SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500

PIPE_GAP = 200


class Leo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # Definindo Sprites do Leo
        self.sprite1 = pygame.image.load("data/image/leo.png").convert_alpha()
        self.sprite2 = pygame.image.load("data/image/leo3.png").convert_alpha()
        self.sprite3 = pygame.image.load("data/image/leo2.png").convert_alpha()
        self.sprite4 = pygame.image.load("data/image/leo3.png").convert_alpha()
        self.sprite5 = pygame.image.load("data/image/leo_mel.png").convert_alpha()
        # Aumentando tamanho dos Sprites
        self.sprite1 = pygame.transform.scale(self.sprite1, [60, 60])
        self.sprite2 = pygame.transform.scale(self.sprite2, [60, 60])
        self.sprite3 = pygame.transform.scale(self.sprite3, [60, 60])
        self.sprite4 = pygame.transform.scale(self.sprite4, [60, 60])
        self.sprite5 = pygame.transform.scale(self.sprite5, [60, 60])
        # Ajustando Sprites no personagem
        self.images = [self.sprite1,
                       self.sprite2,
                       self.sprite3,
                       self.sprite4,
                       self.sprite5
                       ]
        # Declaração da variável que definirá o Sprite
        self.current_image = 0
        # Sprite fixo
        self.image = pygame.image.load("data/image/leo3.png")
        self.speed = 0
        self.acceleration = 0.1
        self.rect = pygame.Rect(50, 50, 60, 60)
        self.timeScore = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.isJump = True

    def update(self, *args):
        if self.isJump:
            self.image = self.images[0]
        else:
            self.current_image = (self.current_image + 1) % 4
            self.image = self.images[self.current_image]

        if self.rect.left < 80:
            self.rect.left = 80
            self.speed = 0
        elif self.rect.right > 500:
            self.rect.right = 500
            self.speed = 0

        # frameAtual = pygame.time.get_ticks()
        # print(frameAtual)
        # self.frameDeTroca = 0
        # if frameAtual > self.frameDeTroca:
        #     self.frameDeTroca += 1000
        #     self.current_image = (self.current_image + 1) % 3
        #     self.image = self.images[self.current_image]
        #     print(clock())
        # else:
        #     print('Frame')
        # Alternando automaticamente cada Sprite do Leo


"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.speed -= self.acceleration
        elif keys[pygame.K_d]:
            self.speed += self.acceleration

        else:
            self.speed *= 0.98

        self.rect.x += self.speed

        if self.rect.left < 30:
            self.rect.left = 30
            self.speed = 0
        elif self.rect.right > 550:
            self.rect.right = 550
            self.speed = 0


        elif keys[pygame.K_SPACE]:
            self.timer -= 0.05
            self.rect.y = 300 + self.timer * 50
            if self.rect.top > 200:
                self.jump = True

        elif self.jump:
            self.timer -= 0.05
            self.rect.y = 400 - self.timer * 50
            self.speed = 0
            print('executando')
            if self.rect.y > 380:
                self.rect.y = 380
                self.jump = False







        elif keys[pygame.KEYUP]:
            self.rect.y -= 10
            print('Solta botao')

        elif keys[pygame.KEYDOWN]:
            self.rect.y += 10
            print('Aperta')

        if keys[pygame.K_SPACE]:
            print('space')

"""

"""
        if keys[pygame.K_SPACE]:
            self.speed += self.acceleration
            jump.play()
        else:
            self.speed *= 0.98
        
        self.rect.y -= self.speed


        if keys[pygame.KEYDOWN]:
            if self.rect == pygame.K_SPACE:
                self.rect.y -= 20
            else:
                if self.rect.y >= - 10:
                    self.speed -= (self.rect.y * abs(self.rect.y)) * 0.5
                else:
                    self.rect.y = 10
                    self.speed = 0
                    
                    
# Meu script 

if keys[pygame.K_a]:
            self.speed -= self.acceleration
        elif keys[pygame.K_d]:
            self.speed += self.acceleration

        else:
            self.speed *= 0.98

        self.rect.x += self.speed

        if self.rect.left < 100:
            self.rect.left = 100
            self.speed = 0
        elif self.rect.right > 630:
            self.rect.right = 630
            self.speed = 0

        if keys[pygame.K_SPACE]:
            isJump = True

        elif keys[pygame.]:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
"""
