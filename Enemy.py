import time

import pygame
import Constants, random, math


class enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.Surface((15, 15))
        self.image.fill(Constants.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, Constants.WIDTH / 2), random.randint(0, Constants.HEIGHT / 2))

    def dodge(self):
        self.speedx = random.randint(-2, 2)
        self.speedy = random.randint(-2, 2)

    def update(self, pls):


        self.dodge()
        if self.rect.x + 20 > Constants.WIDTH or self.rect.x < 20:
            self.speedx = 0
        if self.rect.y + 20 > Constants.HEIGHT or self.rect.y < 20:
            self.speedy = 0

        if (self.rect.x < 0 or self.rect.x > Constants.WIDTH) or (self.rect.y < 0 or self.rect.y > Constants.HEIGHT):
            self.kill()

        self.rect.x += self.speedx
        self.rect.y += self.speedy





