from math import sqrt

class Vector2D:
    def __init__(self, x:float, y:float) -> str:
        """
        Constructeur de la class Vector2D
        Args:
            self: l'objet créé
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
        Args:
            self : un objet de type Vector2D
        Return:
            Le calcul de la norme du vecteur donné en paramètre
        """
        return sqrt(self.x**2 + self.y**2)
    
    def multiply(self, coefficient:int):
        """
        Multiplie un vecteur par un coefficient
        Args:
            self : un objet de type Vector2D
            coefficient : un entier
        Return:
            Ne retourne rien car modifie directement le vecteur donné
        """
        self.x *= coefficient
        self.y *= coefficient

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def scalarProduct(self, vector):
        return self.x*vector.x + self.y*vector.y
    
    def perpendicular(self, vector):
        return self.scalarProduct(vector) == 0
    
    def colinear(self, vector):
        return self.x * vector.y - self.y * vector.x == 0
    
    def __mul__(self, vector):
        return self.scalarProduct(vector)
    
    def __add__(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __repr__(self):
        return f'Vecteur de coordonnées x : {self.x}, y:{self.y}'
    
    def __str__(self) -> str:
        return self.__repr__()
    
v1 = Vector2D(3, 4)