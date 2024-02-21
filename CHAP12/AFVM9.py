import random

class Pile:
    """ classe Pile
    création d'une instance Pile avec une liste
    """
    def __init__(self):
        self.L = []
    def vide(self):
        return self.L == []
    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()
    def sommet(self):
        assert not self.vide(),"Pile vide"
        return self.L[-1]
    def empiler(self,x):
        self.L.append(x)

class File:
    """ classe File
    création d'une instance File avec une liste
    """
    def __init__(self):
        self.L = []
    def vide(self):
        return self.L == []
    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)
    def enfiler(self,x):
        self.L.append(x)
    def taille(self):
        return len(self.L)
    def sommet(self):
        return self.L[0]
    def present(self,x):
        return x in self.L

G = dict()
G['a'] = ['b', 'c']
G['b'] = ['a', 'd', 'e']
G['c'] = ['a', 'd']
G['d'] = ['b', 'c', 'e']
G['e'] = ['b', 'd', 'f', 'g']
G['f'] = ['e', 'g']
G['g'] = ['e', 'f', 'h']
G['h'] = ['g']
G['i'] = []

def voisin(G, sommet):
    return G[sommet]

def parcours_profondeurs(G, sommet):
    """
    Effectue un parcours en profondeur (DFS) sur un graphe non orienté représenté par un dictionnaire d'adjacence.

    Args:
        G (dict): Le graphe représenté par un dictionnaire d'adjacence.
        sommet (str): Le sommet de départ du parcours.

    Returns:
        list: Une liste contenant les sommets visités dans l'ordre du parcours en profondeur.
    """
    pile = Pile()
    pile.empiler(sommet)
    sommets_visites = []
    sommets_visites.append(sommet)
    sommmets_fermes = []
    while not pile.vide():
        tmp = pile.sommet()
        voisins = [y for y in voisin(G,tmp) if y not in sommets_visites]
        if voisins != []:
            v=random.choice(voisins)
            sommets_visites.append(v)
            pile.empiler(v)
        else:
            sommmets_fermes.append(tmp)
            pile.depiler()
    return sommets_visites

sommets_visites = []

def dfs_recursive(G: dict, sommet: str):
    """
    Effectue un parcours en profondeur (DFS) sur un graphe non orienté représenté par un dictionnaire d'adjacence.

    Args:
        G (dict): Le graphe représenté par un dictionnaire d'adjacence.
        sommet (str): Le sommet de départ du parcours.

    Returns:
        list: Une liste contenant les sommets visités dans l'ordre du parcours en profondeur.
    """
    if not sommet in sommets_visites:
        sommets_visites.append(sommet)
    voisins = [y for y in voisin(G, sommet) if y not in sommets_visites]
    for i in voisins:
        dfs_recursive(G, i)
    return sommets_visites

def parcours(end, parents):
    chemin = []
    courant = end
    while courant != None:
        chemin = [courant] + chemin
        courant = parents[courant]
    return chemin

file = File()
source = 'a'
drapeaux = dict(zip(G.keys(), [-1]*len(G)))

print(drapeaux)

def contient_cycle(G):
    """
    Vérifie si un graphe G contient un cycle en utilisant la méthode du parcours en largeur.
    
    Args:
        G (dict): Le graphe représenté sous forme de dictionnaire où les clés sont les sommets et les valeurs sont les listes des voisins.
    
    Returns:
        bool: True si le graphe contient un cycle, False sinon.
    """
    file.enfiler(source)
    while not file.vide():
        sommet = file.defiler()
        drapeaux[sommet] = 1
        for voisin in G[sommet]:
            if drapeaux[voisin] == -1:
                file.enfiler(voisin)
                drapeaux[voisin] = 0
            elif drapeaux[voisin] != 0:
                return True
    return False
            
print(contient_cycle(G))