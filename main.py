import pygame, Constants, Others
from PLayer import Player
import Enemy

pygame.init()
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("Brawl Training")
clock = pygame.time.Clock()
screen.fill(Constants.BLACK)

# Декларация групп объектов
allFig = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enStrikes = pygame.sprite.Group()
plStrikes = pygame.sprite.Group()

me = Player()
fisrtEnemy = Enemy.enemy()

# добавление базовых объектов
allFig.add(me)
enemies.add(fisrtEnemy)

running = True
while running:
    # хз что это
    clock.tick(Constants.FPS)
    # Обработка выхода из программы

    running = Others.playerMoment(me, plStrikes)



    # рендер
    screen.fill(Constants.BLACK)

    enemies.update()
    plStrikes.update()
    me.update()

    allFig.draw(screen)
    plStrikes.draw(screen)
    enemies.draw(screen)

    pygame.display.flip()

pygame.quit()
