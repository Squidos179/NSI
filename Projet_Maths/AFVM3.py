from numpy import sign

def racine_recur(fonc, a, b, p=1e-6):
    """Calcul de la racine d' une fonction par dichotomie
    args :
        - fonc : fonction python
        - a : borne plus petite que la racine
        - b : borne plus grande que la racine
        - p : précision (ou écart max entre la sol. et valeur théorique)
    return :
        - Une valeur approchée de la racine
    """
    x = (a+b)/2
    y = fonc(x)
    if b - a < p:
        return (a, b)
    elif y > 0:
        return racine_recur(fonc, a, x, p)
    else:
        return racine_recur(fonc, x, b, p)

def f(x):
    return x**2 + 3*x

print(racine_recur(f, -4, -2))