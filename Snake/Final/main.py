import pygame
from random import randint
from anneau import Anneau
import snake
import snake2

def collisionSerpents(serpent1, serpent2):
    suivant1 = serpent1.head.suivant
    suivant2 = serpent2.head.suivant

    while suivant2 != None:

        if serpent1.head.x == suivant2.x and serpent1.head.y == suivant2.y:
            return 1
        
        suivant2 = suivant2.suivant

    while suivant1 != None:
        if serpent2.head.x == suivant1.x and serpent2.head.y == suivant1.y:
            return 2
        
        suivant1 = suivant1.suivant

def collision_pomme(serpent1, serpent2 = None):
        global pommex, pommey
        if serpent1.head.x > pommex - 20 and serpent1.head.y > pommey - 20 and serpent1.head.x < pommex + 20 and serpent1.head.y < pommey + 20:
            pommex, pommey = randint(0, 39) * 20, randint(0, 29) * 20
            serpent1.score += 1
            for i in range(5):
                serpent1.head.ajout()
        if serpent2 != None:
            if serpent2.head.x > pommex - 20 and serpent2.head.y > pommey - 20 and serpent2.head.x < pommex + 20 and serpent2.head.y < pommey + 20:
                pommex, pommey = randint(0, 39) * 20, randint(0, 29) * 20
                serpent2.score += 1
                for i in range(5):
                    serpent2.head.ajout()

def damier(colors, surf):
    for i in range(0 , 40):
        for p in range(0, 30):
            pygame.draw.rect(surf, colors[p%2], (i * 20, p * 20, 20, 20))
        colors.reverse()

pommex, pommey = randint(0, 39) * 20, randint(0, 29) * 20

jaaj = snake.Serpent()
jaaj.head.x = 400
jaaj.head.y = 300

response = False
mode = None

while response != True:

    mode = input("Voulez-vous à 1 ou 2 joueurs ? (Tapez 1 ou 2) : ")

    if mode == '1':
        response = True
    elif mode == '2':
        response = True
        jeej = snake2.Serpent2()
        jeej.head.x = 600
        jeej.head.y = 300
        jaaj.head.x = 200
        jaaj.head.y = 300   
    else:
        print('Réponse incorrect, veuillez tapez 1 ou 2')

pygame.init()
pygame.font.init()

surf = pygame.display.set_mode((800, 600))
run = True
clock = pygame.time.Clock()
scoreFont = pygame.font.SysFont(None, 30)
colors = [(0x0B, 0x8E, 0x3F), (0x35, 0xAE, 0x3B)]

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)

    damier(colors, surf)
    pygame.draw.rect(surf, (255, 0, 0), (pommex, pommey, 20, 20))
        
    jaaj.update()
    jaaj.render(surf, scoreFont)

    if mode == '1':
        collision_pomme(jaaj)

    if mode == '2':

        jeej.update()
        collision_pomme(jaaj, jeej)
        jeej.render(surf, scoreFont)

        result = collisionSerpents(jaaj, jeej)

        if result == 1:
            jaaj.gameOver()
        elif result == 2:
            jeej.gameOver()

    pygame.display.flip()
pygame.quit()