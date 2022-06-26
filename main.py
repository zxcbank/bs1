import pygame, Constants, Others
from PLayer import Player
import Enemy
import time

pygame.init()
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("Brawl Training")
clock = pygame.time.Clock()
screen.fill(Constants.BLACK)

# Декларация групп объектов
plGroup = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enStrikes = pygame.sprite.Group()
plStrikes = pygame.sprite.Group()

me = Player()
fisrtEnemy = Enemy.enemy()

# добавление базовых объектов
plGroup.add(me)
enemies.add(fisrtEnemy)

# переменные для перезарядок

running = True

while running:
    # хз что это

    clock.tick(Constants.FPS)
    # Обработка всех событий
    running= Others.eventMoment(me, plStrikes, enemies)

    # обновления
    enemies.update(plStrikes) # обновление позиции врагов
    plStrikes.update() # обновление позиций пуль игрока
    me.update() # обновление позиции игрока

    # рендер
    screen.fill(Constants.BLACK)
    plGroup.draw(screen) # отрисовка игрока
    plStrikes.draw(screen) # отрисовка пуль игрока
    enemies.draw(screen) # отрисовка позиций врагов

    pygame.display.flip() # двойная буферизация

pygame.quit()
