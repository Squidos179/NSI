from numpy import sign

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
        if sign(fonc(a)) == sign(fonc(b)):
            raise Exception
    except Exception:
        print("Les bornes données ne sont pas bonnes")
    else:
        jaaj = b - a
        while jaaj > p:
            x = (a+b)/2
            y = fonc(x)
            if y > 0:
                b = x
            else:
                a = x
            jaaj = b - a
        return (a, b)
        
def f(x):
    return x**2 + 3*x

print(racine(f, -3.5, -2.5))