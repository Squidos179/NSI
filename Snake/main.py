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
x, y = 400, 300
clock = pygame.time.Clock()
vec2D =[0, 0]
snakes = [snake.Snake()]
xr, yr = randint(0, 800), randint(0, 600)
score = 0
scoreFont = pygame.font.SysFont(None, 30)
scoreText = scoreFont.render(str(score), True, (255, 255, 255))
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    surf.fill((0, 0, 0))
    for i in snakes:
        pygame.draw.rect(surf, (255, 255, 255), (i.x, i.y, 5, 5))
    pygame.draw.rect(surf, (255, 0, 0), (xr, yr, 10, 10))
    scoreText = scoreFont.render(str(score), True, (255, 255, 255))
    surf.blit(scoreText, (20, 20))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        vec2D[0] = -3
        vec2D[1] = 0
    if keys[pygame.K_d]:
        vec2D[0] = 3
        vec2D[1] = 0
    if keys[pygame.K_z]:
        vec2D[0] = 0
        vec2D[1] = -3
    if keys[pygame.K_s]:
        vec2D[0] = 0
        vec2D[1] = 3
    snakes[0].x += vec2D[0]
    snakes[0].y += vec2D[1]
    if x > xr and y > yr and x < xr + 10 and y < yr + 10:
        xr, yr = randint(0, 800), randint(0, 600)
        score += 1
        snakes.append(snake.Snake())
    if x > 800 or x < 0 or y > 600 or y < 0:
        score = 0
        x, y = 400, 300
        vec2D = [0, 0]
    pygame.display.flip()
pygame.quit()