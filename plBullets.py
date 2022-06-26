import pygame
import Constants
import time


class plStrike(pygame.sprite.Sprite):

    def __init__(self, x, y, tx, ty):
        pygame.sprite.Sprite.__init__(self)
        dX, dY = tx - x, ty - y
        self.image = pygame.Surface((5, 5))
        self.image.fill(Constants.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.tx, self.ty = tx, ty
        self.speedx, self.speedy = None, None
        self.lp = 1
        self.startTime = time.time()

        try:
            self.speedx = (Constants.V ** 2) / (1 + abs(dY / dX)) * (dX / abs(dX))
        except ZeroDivisionError:
            self.speedx = 0
        try:
            self.speedy = (Constants.V ** 2) / (1 + abs(dX / dY)) * (dY / abs(dY))
        except ZeroDivisionError:
            self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.y > Constants.HEIGHT or self.rect.y < 0) or (
                self.rect.x > Constants.WIDTH or self.rect.x < 0) or (self.speedx == 0 and self.speedy == 0) or (
                time.time() > self.lp + self.startTime):
            self.kill()
