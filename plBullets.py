import pygame
import Constants

class plBullet (pygame.sprite.Sprite):

    def __init__(self, x, y, tx, ty):
        pygame.sprite.Sprite.__init__(self)
        dX, dY = tx - x, ty - y
        self.image = pygame.Surface((5, 5))
        self.image.fill(Constants.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.tx = tx
        self.ty = ty
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
        if (self.rect.y > Constants.HEIGHT or self.rect.y < 0) or (self.rect.x > Constants.WIDTH or self.rect.x < 0) or (self.speedx == 0 and self.speedy == 0):
            self.kill()
        if self.rect.x + 3 > self.tx > self.rect.x - 3:
            self.speedx = 0
        if self.rect.y + 3 > self.ty > self.rect.y - 3:
            self.speedy = 0