# -*- coding: utf-8 -*-
from math import sqrt
import timeit
def factorielClassique(n) :
    """
        >>> factorielClassique(5)
        120
        >>> factorielClassique(0)
        1
    """
    resultat = 1
    while n > 0:
        resultat *= n
        n -= 1
    return resultat

def factorielRecursive(n) :
    if n > 0 :
        return n*factorielRecursive(n-1)
    else :
        return 1

if __name__=='__main__':
    tps = timeit.timeit("factorielClassique(10)", number = 1000000, globals=globals())
    print(f"Temps écoulé pour 1 000 000 exécution de la fonction : {tps} ")
    tps2 = timeit.timeit("factorielRecursive(10)", number = 1000000, globals=globals())
    print(f"Temps écoulé pour 1 000 000 exécution de la fonction : {tps2} ")