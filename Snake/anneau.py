import pygame
from random import randint

class Anneau:
    rect = [5, 5]
    x = -1000
    y = -1000
    fx = 300
    fy = 300
    suivant = None

    def update(self, vec2D):
        self.fx = self.x +  vec2D[0] * 20
        self.fy = self.y +  vec2D[1] * 20
        if self.suivant != None:
            self.suivant.fx = self.x
            self.suivant.fy = self.y

            self.x = self.fx
            self.y = self.y

            self.suivant.x = self.suivant.fx
            self.suivant.y = self.suivant.fy

    def render(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.x, self.y, 20, 20))
        if self.suivant != None:
            self.suivant.render()

        