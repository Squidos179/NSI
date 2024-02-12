import pygame

LARG, HAUT = 20, 20
MULTIPLE = 34

def damier(colors, surf):
    for i in range(0 , MULTIPLE):
        for p in range(0, MULTIPLE):
            pygame.draw.rect(surf, colors[p%2], (i * LARG, p * HAUT, LARG, HAUT))
        colors.reverse()

def dessine_serpent(surf, x, y):
    pygame.draw.rect(surf, (255, 255, 255), (x, y, 20, 20))

def clavier(vec2D):
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

pygame.init()
pygame.font.init()

surf = pygame.display.set_mode((MULTIPLE * LARG, MULTIPLE * HAUT))
run = True
clock = pygame.time.Clock()
colors = [(0x0B, 0x8E, 0x3F), (0x35, 0xAE, 0x3B)]
x, y = 10 * MULTIPLE, 10 * MULTIPLE
vec2D = [0, 0]

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)
    clavier(vec2D)

    x += LARG * vec2D[0]
    y += HAUT * vec2D[1]

    damier(colors, surf)
    dessine_serpent(surf, x, y)

    pygame.display.flip()
pygame.quit()