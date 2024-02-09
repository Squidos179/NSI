import pygame
from random import randint
from anneau import Anneau
import snake

pygame.init()
pygame.font.init()
surf = pygame.display.set_mode((800, 600))
run = True
clock = pygame.time.Clock()
xr, yr = randint(0, 39) * 20, randint(0, 29) * 20
score = 0
scoreFont = pygame.font.SysFont(None, 30)
scoreText = scoreFont.render(str(score), True, (255, 255, 255))

snake.Serpent()

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(20)

    for i in range(0 , 800, 40):
        for p in range(0, 600, 40):
            pygame.draw.rect(surf, (0x0B, 0x8E, 0x3F), (i, p, 20, 20))
    for i in range(20, 800, 40):
        for p in range(20, 600, 40):
            pygame.draw.rect(surf, (0x0B, 0x8E, 0x3F), (i, p, 20, 20))

    for i in range(0 ,800, 40):
        for p in range(20, 600, 40):
            pygame.draw.rect(surf, (0x35, 0xAE, 0x3B), (i, p, 20, 20))
    for i in range(20, 800, 40):
        for p in range(0, 600, 40):
            pygame.draw.rect(surf, (0x35, 0xAE, 0x3B), (i, p, 20, 20))

    pygame.draw.rect(surf, (255, 0, 0), (xr, yr, 20, 20))
    scoreText = scoreFont.render(str(score), True, (255, 255, 255))
    surf.blit(scoreText, (20, 20))

    

    pygame.display.flip()
pygame.quit()