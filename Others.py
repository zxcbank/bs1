import pygame, Constants, plBullets

def playerMoment(ASD, plStrikes):
    x = None
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] is True:
            ASD.speedx = -3
        elif keys[pygame.K_d] is True:
            ASD.speedx = 3
        else:
            ASD.speedx = 0
        if keys[pygame.K_w] is True:
            ASD.speedy = -3
        elif keys[pygame.K_s] is True:
            ASD.speedy = 3
        else:
            ASD.speedy = 0

        #обработка для пуль
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            plStrikes.add(plBullets.plBullet(ASD.rect.x, ASD.rect.y, pos[0], pos[1]))

    return True