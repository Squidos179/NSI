import pygame
from random import randint
from anneau import Anneau

class Serpent:

    def __init__(self) -> None:

        self.head = Anneau()

    def gameOver(self):
        self.head.x, self.head.y = 400, 300
        self.vec2D = [0, 0]
        self.head.suivant = None
        self.px, self.py = randint(0, 39) * 20, randint(0, 29) * 20

    def update(self):
        suivant = self.head.suivant

        while suivant != None:

            suivant.fx = suivant.avant.x
            suivant.fy = suivant.avant.y

            suivant = suivant.suivant

        self.head.update()

        suivant = self.head.suivant

        while suivant != None:

            suivant.update()

            suivant = suivant.suivant


    def dessine_serpent(self, surf):
        self.head.dessine_anneau(surf)