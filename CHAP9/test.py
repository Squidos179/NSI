from random import randint

def attendre_doublon_liste(n):
    liste = []
    while True:
        h = randint(1, n)
        if h in liste:
            liste.append(h)
            return len(liste)
        else:
            liste.append(h)

def attendre_doublon_set(n):
    liste = set()
    while True:
        h = randint(1, n)
        if h in liste:
            liste.add(h)
            return len(liste)
        else:
            liste.add(h)

def temps_attente(n, nb):
    temps = 0
    for i in range(nb):
        temps += attendre_doublon_liste(n)
    return temps/nb

print(temps_attente(10**6, 10000))