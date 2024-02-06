import pygame
from random import randint
import snake

def keyHandling(x , y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        x -= 3
    if keys[pygame.K_d]:
        x += 3
    if keys[pygame.K_z]:
        y -= 3
    if keys[pygame.K_s]:
        y += 3

pygame.init()
pygame.font.init()
surf = pygame.display.set_mode((800, 600))
run = True
clock = pygame.time.Clock()
vec2D =[0, 0]
snakes = [snake.Snake()]
xr, yr = randint(0, 39) * 20, randint(0, 29) * 20
score = 0
scoreFont = pygame.font.SysFont(None, 30)
scoreText = scoreFont.render(str(score), True, (255, 255, 255))
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(20)
    surf.fill((0, 0, 0))
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
    for i in snakes:
        pygame.draw.rect(surf, (255, 255, 255), (i.x, i.y, 20, 20))
    pygame.draw.rect(surf, (255, 0, 0), (xr, yr, 20, 20))
    scoreText = scoreFont.render(str(score), True, (255, 255, 255))
    surf.blit(scoreText, (20, 20))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and vec2D[0] != 1:
        vec2D[0] = -1
        vec2D[1] = 0
    if keys[pygame.K_RIGHT] and vec2D[0] != -1:
        vec2D[0] = 1
        vec2D[1] = 0
    if keys[pygame.K_UP] and vec2D[1] != 1:
        vec2D[0] = 0
        vec2D[1] = -1
    if keys[pygame.K_DOWN] and vec2D[1] != -1:
        vec2D[0] = 0
        vec2D[1] = 1
    
    snakes[0].fx = snakes[0].x +  vec2D[0] * 20
    snakes[0].fy = snakes[0].y +  vec2D[1] * 20

    for i in range(1, len(snakes)):
        snakes[i].fx = snakes[i - 1].x
        snakes[i].fy = snakes[i - 1].y

    snakes[0].x = snakes[0].fx
    snakes[0].y = snakes[0].fy

    for i in range(1, len(snakes)):
        snakes[i].x = snakes[i].fx
        snakes[i].y = snakes[i].fy

    if snakes[0].x > xr -20 and snakes[0].y > yr - 20 and snakes[0].x < xr + 20 and snakes[0].y < yr + 20:
        xr, yr = randint(0, 39) * 20, randint(0, 29) * 20
        score += 1
        snakes.append(snake.Snake())
    if snakes[0].x > 780 or snakes[0].x < 0 or snakes[0].y > 580 or snakes[0].y < 0:
        score = 0
        snakes[0].x, snakes[0].y = 400, 300
        vec2D = [0, 0]
        for i in range(len(snakes) - 1, 0, -1):
            del(snakes[i])
    for i in snakes[1:]:
        if snakes[0].x == i.x and snakes[0].y == i.y:
            score = 0
            snakes[0].x, snakes[0].y = 400, 300
            vec2D = [0, 0]
            for i in range(len(snakes) - 1, 0, -1):
                del(snakes[i])
    pygame.display.flip()
pygame.quit()