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

def voisins(G, sommet):
    return G[sommet]


def bfs(G : dict):
    """
    Effectue un parcours en largeur (BFS) sur un graphe non orienté représenté par un dictionnaire d'adjacence.

    Args:
        G (dict): Le graphe représenté par un dictionnaire d'adjacence.

    Returns:
        list: Une liste contenant les sommets visités dans l'ordre du parcours en largeur.
    """
    jaaj = File()
    jaaj.enfiler(list(G.keys())[0])
    tmp = None
    sommets_visites = []
    while not jaaj.vide():
        tmp = jaaj.defiler()
        if not tmp in sommets_visites:
            sommets_visites.append(tmp)
            for i in voisins(G, tmp):
                if not i in sommets_visites and not jaaj.present(i):
                    jaaj.enfiler(i)
    return sommets_visites

def bfs_recur(G : dict, f : File, sommets_visites : list):
    """
    Effectue un parcours en largeur d'abord (BFS) de manière récursive sur un graphe.

    Args:
        G (graph): Le graphe sur lequel effectuer le BFS.
        f (queue): La file utilisée pour le parcours BFS.
        sommets_visites (list): La liste des sommets visités.

    Returns:
        None
    """
    if f.vide():
        return None
    tmp = f.defiler()
    print(tmp, end=" ")
    for u in voisins(G, tmp):
        if u not in sommets_visites:
            sommets_visites
            f.enfiler(u)
    bfs_recur(G, f, sommets_visites)

f = File()
sommets_visites = []
sommet = 'b'
f.enfiler(sommet)
sommets_visites.append(sommet)
bfs_recur(G, f, sommets_visites)

print(sommets_visites)