import pygame


class Leo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.time = 0
        self.images = [pygame.image.load("data/image/leo.png"),
                       pygame.image.load("data/image/leo2.png"),
                       pygame.image.load("data/image/leo3.png")
                       ]
        self.current_image = 0
        # self.image = pygame.transform.scale(self.images[-1], [100, 100])
        self.image = pygame.image.load("data/image/leo3.png")
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.timeScore = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        self.timeScore += 0.01
        self.time = int(self.timeScore)
        if self.time == self.timeScore + 1:
            self.current_image = (self.current_image + 1) % 3
            self.image = self.images[self.current_image]



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
