from __future__ import annotations
from math import sqrt

class Vector2D:
    def __init__(self, x:float, y:float)->None:
        """
        Constructeur de la class Vector2D
        Args:
            x : un décimal
            y: un décimal
        Return:
            Ne retourne rien
        """
        try:
            if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float):
                raise TypeError
        except TypeError:
            print("Les valeurs entrées pour le vecteur sont autres que des entiers ou des décimaux, veuillez réessayer.")
        else:
            self.x = x
            self.y = y

    def norm(self)->float:
        """
        Donne la norme d'un vecteur
        Return:
            Le calcul de la norme du vecteur donné en paramètre
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
        except TypeError:
            print("Les valeurs entrées pour le vecteur sont autres que des entiers ou des décimaux, veuillez réessayer.")
        else:
            return sqrt(self.x**2 + self.y**2)
    
    def multiply(self, coefficient:float)->None:
        """
        Multiplie un vecteur par un coefficient
        Args:
            coefficient : un décimal
        Return:
            Ne retourne rien car modifie directement le vecteur donné
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(coefficient) != int and type(coefficient) != float:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            self.x *= coefficient
            self.y *= coefficient

    def add(self, vector:Vector2D)->None:
        """
        Ajoute à un vecteur un autre vecteur
        Args:
            vector : un objet de type Vector2D
        Return:
            Ne retourne rien car modifie directement le vecteur donné
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError:
            print("Les valeurs entrées pour le vecteur sont autres que des entiers ou des décimaux, veuillez réessayer.")
        else:
            self.x += vector.x
            self.y += vector.y

    def scalarProduct(self, vector:Vector2D)->float:
        """
        Calcul le produit scalaire de deux vecteur
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un décimal qui est le produit scalaire du vecteur et d'un autre vecteur
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            return self.x*vector.x + self.y*vector.y
    
    def perpendicular(self, vector:Vector2D)->bool:
        """
        Permet de savoir le vecteur et un autre vecteur sont perpendiculaire
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne True si les deux vecteurs sont perpendiculaires et False si ce n'est pas le cas
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            return self.scalarProduct(vector) == 0
    
    def colinear(self, vector:Vector2D)->bool:
        """
        Permet de savoir le vecteur et un autre vecteur sont colinéaire
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne True si les deux vecteurs sont colinéaires et False si ce n'est pas le cas
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            return self.x * vector.y - self.y * vector.x == 0
    
    def __mul__(self, vector:Vector2D)->float:
        """
        Permet de gérer un cas de multiplication de deux vecteurs
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un décimal qui est le résultat de la fonction "scalarProduct" avec en paramètre 'vector'
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            return self.scalarProduct(vector)
    
    def __add__(self, vector:Vector2D) -> Vector2D:
        """
        Permet de gérer un cas d'addition de deux vecteurs
        Args:
            vector : Un objet de type Vector2D
        Return:
            Retourne un nouvel objet de type Vector2D avec en attribut l'addition de deux vecteurs
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
            if type(vector) != Vector2D:
                raise TypeError
        except TypeError as error:
            print(error)
        else:
            return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __repr__(self)->str:
        """
        Represente le vecteur avec un string
        
        Return:
            Retourne un string qui donne les valeurs du vecteur
        """
        return f'Vecteur de coordonnées x : {self.x}, y : {self.y}'
    
    def __str__(self) -> str:
        """
        Ce que retourne un print() avec un vecteur en argument

        Return:
            Retourne la même chose que le __repr__ donc un string qui donne les valeurs du vecteur
        """
        try:
            if (type(self.x) != int and type(self.x) != float) or (type(self.y) != int and type(self.y) != float):
                raise TypeError
        except TypeError:
            print("Les valeurs entrées pour le vecteur sont autres que des entiers ou des décimaux, veuillez réessayer.")
        else:
            return self.__repr__()
    
# Création de vecteurs pour les tests
vec1 = Vector2D(3.0, 4)
vec2 = Vector2D(5, 12)
vec3 = Vector2D(1, 1)
vec4 = Vector2D(-3, -4)

# Test de la méthode norm()
assert vec1.norm() == 5.0
assert vec2.norm() == 13.0
assert vec3.norm() == sqrt(2)
assert vec4.norm() == 5.0

# Test de la méthode multiply()
vec1.multiply(2)
assert vec1.x == 6 and vec1.y == 8

# Test de la méthode add()
resultant_vec = vec2 + vec3
assert resultant_vec.x == 6 and resultant_vec.y == 13

# Test de la méthode scalarProduct()
assert vec1 * vec2 == 126
assert vec1 * vec3 == 14
assert vec1 * vec4 == -50

# Test de la méthode perpendicular()
assert vec1.perpendicular(vec3) == False  # Devrait être False (produit scalaire = 14)

# Test de la méthode colinear()
assert vec1.colinear(vec2) == False  # Devrait être False

print("Tous les tests ont été exécutés avec succès !")