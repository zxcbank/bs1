import pygame, Constants, plBullets, time


def eventMoment(player, plStrikes, enemies):
    x = None
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            return False

        # изменение скорости игрока в завимсимости от клавиш
        player.vchange(pygame.key.get_pressed())

        # обработка для пуль
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            plStrikes.add(plBullets.plStrike(player.rect.x, player.rect.y, pos[0], pos[1]))

        #обработка жизни врагов
        for _ in enemies:
            for i in plStrikes:
                if (_.rect.x + 15 >= i.rect.x >= _.rect.x) and (_.rect.y + 15 >= i.rect.y >= _.rect.y):
                    _.kill()
                    i.kill()

    return True
