def applique(f, l:list)->list:
    res = []
    for i in l:
        res.append(f(i))
    return res

def maj(feur:str)->str:
    return feur.upper()

#print(applique(maj, ['jaaj', 'feur']))

mystere = lambda liste: applique(lambda nb: nb**2, liste)

# Question C : On l'utilise avec mystere(liste) comme une funcion normale Ex : mystere([3, 0, 67, 3, 4])

majuscule = lambda liste: applique(maj, liste)

#print(majuscule(['jaaj', 'feur']))

def reduit(fonction, depart, liste:list):
    for i in liste:
        depart = fonction(depart, i)
    return depart

def tous_vrais(liste:list)->bool: return reduit(lambda x, y: x+y, 0, liste) == len(liste)

def taille(liste:list)->int: return reduit(lambda x, y: x+1, 0, liste)

#print(tous_vrais([3>2, len('jaa') == 4]))

#print(taille([3, 4, 5, 2, 4]))

def filtre(func, liste:list)->list:
    pass