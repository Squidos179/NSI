import pygame
import snake

LARG, HAUT = 20, 20
MULTIPLE = 34

def damier(colors, surf):
    for i in range(0 , MULTIPLE):
        for p in range(0, MULTIPLE):
            pygame.draw.rect(surf, colors[p%2], (i * LARG, p * HAUT, LARG, HAUT))
        colors.reverse()

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

vec2D = [0, 0]

jaaj = snake.Serpent()
jaaj.head.x = 200
jaaj.head.y = 200

for i in range(5):
    jaaj.head.ajout()

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)

    damier(colors, surf)

    clavier(vec2D)

    jaaj.head.fx = jaaj.head.x + 20 * vec2D[0]
    jaaj.head.fy = jaaj.head.y + 20 * vec2D[1]

    jaaj.update()

    jaaj.dessine_serpent(surf)

    pygame.display.flip()
pygame.quit()