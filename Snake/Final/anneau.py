import pygame
from random import randint

class Anneau:

    def __init__(self, avant = None) -> None:
        """
        Initialise un objet Anneau.
        Args:
            avant (Anneau): Anneau précédent, par défaut égal à None pour quand on crée la tête.
        Returns:
            None : on crée un objet Anneau.
        """
        self.x = -1000
        self.y = -1000
        self.fx = 0
        self.fy = 0
        self.suivant = None
        self.avant = avant

    def update(self):
        """
        Met à jour les coordonnées de l'anneau en fonction des nouvelles coordonnées fournies.
        Si l'anneau a un anneau suivant, met également à jour les coordonnées de l'anneau suivant.
        Returns:
            None : on modifie directement les attributs de l'anneau.
        """
        self.x = self.fx
        self.y = self.fy

        if self.suivant != None:
            self.suivant.update()

    def render(self, surf, color):
        """
        Dessine l'anneau sur la surface donnée.
        Args:
            surf (pygame.Surface): La surface sur laquelle on dessine.
            color (tuple): La couleur de l'anneau.
        Returns:
            None : on modifie directement la surface.
        """
        pygame.draw.rect(surf, color, (self.x, self.y, 20, 20))
        if self.suivant != None:
            self.suivant.render(surf, color)

    def ajout(self):
        """
        Ajoute un nouvel anneau à la suite de l'anneau actuel.

        Si l'anneau suivant est None, crée un nouvel anneau et le définit comme l'anneau suivant.
        Sinon, appelle récursivement la méthode ajout sur l'anneau suivant.

        Returns:
            None : on modifie directement les attributs des anneaux.
        """
        if self.suivant == None:
            self.suivant = Anneau(self)
        else:
            self.suivant.ajout()
