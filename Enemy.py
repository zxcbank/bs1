import pygame
import Constants, random


class enemy (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(Constants.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, Constants.WIDTH / 2),random.randint(0, Constants.HEIGHT / 2))