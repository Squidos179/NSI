import pygame
from random import randint
from anneau import Anneau

class Serpent:

    def __init__(self) -> None:

        self.head = Anneau()

        self.vec2D = [0, 0]

        self.score = 0

    def keyHandling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.vec2D[0] != 1:
            self.vec2D[0] = -1
            self.vec2D[1] = 0
        if keys[pygame.K_RIGHT] and self.vec2D[0] != -1:
            self.vec2D[0] = 1
            self.vec2D[1] = 0
        if keys[pygame.K_UP] and self.vec2D[1] != 1:
            self.vec2D[0] = 0
            self.vec2D[1] = -1
        if keys[pygame.K_DOWN] and self.vec2D[1] != -1:
            self.vec2D[0] = 0
            self.vec2D[1] = 1

    def gameOver(self):
        self.score = 0
        self.head.x, self.head.y = 400, 300
        self.vec2D = [0, 0]
        self.head.suivant = None
        self.px, self.py = randint(0, 39) * 20, randint(0, 29) * 20

    def collision(self):
        suivant = self.head.suivant

        while suivant != None:

            if self.head.x == suivant.x and self.head.y == suivant.y:
                self.gameOver()
            
            suivant = suivant.suivant

        if self.head.x > 780 or self.head.x < 0 or self.head.y > 580 or self.head.y < 0:
            self.gameOver()

    def update(self):
        suivant = self.head.suivant
        self.keyHandling()
        self.collision()
        self.head.fx = self.head.x + 20 * self.vec2D[0]
        self.head.fy = self.head.y + 20 * self.vec2D[1]


        while suivant != None:

            suivant.fx = suivant.avant.x
            suivant.fy = suivant.avant.y

            suivant = suivant.suivant

        self.head.update()

        suivant = self.head.suivant

        while suivant != None:

            suivant.update()

            suivant = suivant.suivant

    def render(self, surf, scoreFont):
        self.head.render(surf)

        scoreText = scoreFont.render(str(self.score), True, (255, 255, 255))
        surf.blit(scoreText, (20, 20))