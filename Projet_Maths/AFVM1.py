from math import sqrt
from numpy import sign

def equation_second_degre(a, b, c):
    """Calcul de la racine d' une équation du 2nd degré ax²+bx+c
    @params :
    - a : coef du terme de degré 2
    - b : coef du terme de degré 1
    - c : coef du terme de degré 0
    @returns :
    - 2 ou 1 ou None
    """
    try:
        if (type(a) != float and type(a) != int) or (type(b) != float and type(b) != int) or (type(c) != float and type(c) != int):
            raise TypeError
    except TypeError:
        print("Les valeurs entrées ne sont pas bonnes")
    else:
        delta = b**2 - (4*a*c)
        if delta < 0:
            solution = "Pas de solution réelle"
        if delta == 0:
            solution = -b/(2*a)
        else:
            solution = ((-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a))
            print(delta)
    return solution