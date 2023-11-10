from __future__ import annotations
from math import sqrt

class Vector2D:
    def __init__(self, x:float, y:float) -> str:
        """
        Constructeur de la class Vector2D
        Args:
            x : un décimal
            y: un décimal
        Return:
            Ne retourne rien
        """
        self.x = x
        self.y = y
        print(self)

    def norm(self):
        """
        Donne la norme d'un vecteur
        Return:
            Le calcul de la norme du vecteur donné en paramètre
        """
        return sqrt(self.x**2 + self.y**2)
    
    def multiply(self, coefficient:int):
        """
        Multiplie un vecteur par un coefficient
        Args:
            coefficient : un entier
        Return:
            Ne retourne rien car modifie directement le vecteur donné
        """
        self.x *= coefficient
        self.y *= coefficient

    def add(self, vector):
        """
        Ajoute à un vecteur un autre vecteur
        Args:
            self : un objet de type Vector2D auquel on va ajouter un autre Vector2D
        Return:
            Ne retourne rien car modifie directement le vecteur donné
        """
        self.x += vector.x
        self.y += vector.y

    def scalarProduct(self, vector):
        """
        Calcul le produit scalaire de deux vecteur
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un décimal qui est le produit scalaire du vecteur et d'un autre vecteur
        """
        return self.x*vector.x + self.y*vector.y
    
    def perpendicular(self, vector):
        """
        Permet de savoir le vecteur et un autre vecteur sont perpendiculaire
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne True si les deux vecteurs sont perpendiculaires et False si ce n'est pas le cas
        """
        return self.scalarProduct(vector) == 0
    
    def colinear(self, vector):
        """
        Permet de savoir le vecteur et un autre vecteur sont colinéaire
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne True si les deux vecteurs sont colinéaires et False si ce n'est pas le cas
        """
        return self.x * vector.y - self.y * vector.x == 0
    
    def __mul__(self, vector):
        """
        Permet de gérer un cas de multiplication de deux vecteurs
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un décimal qui est le résultat de la fonction "scalarProduct" avec en paramètre 'vector'
        """
        return self.scalarProduct(vector)
    
    def __add__(self, vector):
        """
        Permet de gérer un cas d'addition de deux vecteurs
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un nouvel objet de type Vector2D avec en attribut l'addition de deux vecteurs
        """
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __repr__(self):
        """
        Represente le vecteur avec un string
        
        Return:
            Retourne un string qui donne les valeurs du vecteur
        """
        return f'Vecteur de coordonnées x : {self.x}, y:{self.y}'
    
    def __str__(self) -> str:
        """
        Ce que retourne un print() avec un vecteur en argument

        Return:
            Retourne la même chose que le __repr__ donc un string qui donne les valeurs du vecteur
        """
        return self.__repr__()
    
v1 = Vector2D(3, 4)