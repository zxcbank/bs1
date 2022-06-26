import pygame
import Constants


class Player (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Constants.WIDTH / 2, Constants.HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def vchange(self, keys):
        if keys[pygame.K_a] is True:
            self.speedx = -3
        elif keys[pygame.K_d] is True:
            self.speedx = 3
        else:
            self.speedx = 0
        if keys[pygame.K_w] is True:
            self.speedy = -3
        elif keys[pygame.K_s] is True:
            self.speedy = 3
        else:
            self.speedy = 0




