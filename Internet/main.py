from math import sin, pi
import pygame

loop = 0

pygame.init()

surf = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    surf.fill((0, 0, 0))
    loop += pi/500
    pygame.draw.rect(surf, (255, 255, 255), (200 - 15, 200 + sin(loop) * 30, 30, 30))
    pygame.draw.rect(surf, (255, 255, 255), (200 - 15, 280, 30, 110))
    pygame.display.flip()