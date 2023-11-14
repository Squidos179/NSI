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

print(factorielClassique(5))