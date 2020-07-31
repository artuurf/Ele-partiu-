import pygame
import math


class Leo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/image/leo.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.speed = 0
        self.acceleration = 0.1



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
