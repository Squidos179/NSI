import pygame
from random import randint

class Anneau:

    def __init__(self, avant = None) -> None:

        self.x = -1000
        self.y = -1000
        self.fx = 0
        self.fy = 0
        self.suivant = None
        self.avant = avant

    def update(self):
        self.x = self.fx
        self.y = self.fy

        if self.suivant != None:
            
            self.suivant.update()

    def dessine_anneau(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.x, self.y, 20, 20))
        if self.suivant != None:
            self.suivant.dessine_anneau(surf)

    def ajout(self):
        if self.suivant == None:
            self.suivant = Anneau(self)
        else:
            return self.suivant.ajout()