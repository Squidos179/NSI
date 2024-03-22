def derive(fonc, a, h=1e-3, p=1e-6):
    """Calcul du nombre dérivé d' un fonction en un point
    On divise par deux l' intervalle à chaque itération
    @params :
    - fonc : fonction python
    - a : point dont on veut la valeur du dérivé
    - h : écart initial
    - p : précision voulue (ou écart entre deux valeurs de dérivé
    successives)
    @returns :
    - Une valeur approchée du nombre dérivé
    >>> derive(lambda x:x**2, 3)
    6
    >>> derive(lambda x:x**3, 2)
    12
    """
    try:
        derivation = (fonc(a+h)-fonc(a))/h
        if derivation < p:
            raise Exception
    except Exception:
        print("Une valeur n'est pas bonne")
    else:
        while h > p:
            h /= 2
            derivation = (fonc(a+h)-fonc(a))/h
        return derivation

def f(x):
    return x**2

print(derive(f, 7))