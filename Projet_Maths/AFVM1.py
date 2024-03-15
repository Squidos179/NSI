from math import sqrt, sign

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

def racine(fonc, a, b, p=1e-6):
    """Calcul de la racine d' une fonction par dichotomie
    @params :
    - fonc : fonction python
    - a : borne plus petite que la racine
    - b : borne plus grande que la racine
    - p : précision (ou écart max entre la sol. et valeur théorique)
    @returns :
    - Une valeur approchée de la racine
    """
    try:
        if sign(fonc(a)) != sign(fonc(b)):
            raise Exception
    except Exception:
        print("Les bornes données ne sont pas bonnes")
    else:
        jaaj = b - a
        while jaaj > p:
            center = (b+a)/2
            i = fonc(center)
            jaaj = b - a
            s = sign(i)
    #Vérification que les images fonc(a) et fonc(b) sont bien de signes contraires
    #Calcul itératif
    return solution

print(equation_second_degre(1, 3 ,0))