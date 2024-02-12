import pygame

LARG, HAUT = 20, 20
MULTIPLE = 34

def damier(colors, surf):
    for i in range(0 , MULTIPLE):
        for p in range(0, MULTIPLE):
            pygame.draw.rect(surf, colors[p%2], (i * LARG, p * HAUT, LARG, HAUT))
        colors.reverse()

pygame.init()
pygame.font.init()

surf = pygame.display.set_mode((MULTIPLE * LARG, MULTIPLE * HAUT))
run = True
clock = pygame.time.Clock()
colors = [(0x0B, 0x8E, 0x3F), (0x35, 0xAE, 0x3B)]

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)

    damier(colors, surf)

    pygame.display.flip()
pygame.quit()