class Pile:
    def __init__(self) -> None:
        self.liste = []

    def est_vide(self) -> bool:
        return self.liste == []
    
    def empiler(self, value) -> None:
        self.liste.append(value)

    def depiler(self):
        r = self.liste[len(self.liste) - 1]
        del(self.liste[len(self.liste) - 1])
        return r

#1. 8, 5, 2, 4 (8 est l'élément du haut)

#2.

def hauteur_pile(pile:Pile)-> int:
    Q = Pile()
    n = 0
    while not pile.est_vide():
        n += 1
        x = pile.depiler()
        Q.empiler(x)
    while not Q.est_vide():
        x = Q.depiler()
        pile.empiler(x)
    return n

def max_pile(pile:Pile, i:int):
    y = pile.depiler()
    pile.empiler(y)
    Q = Pile()
    r = 0
    for i in range(i):
        x = pile.depiler()
        if x > y:
            r = i  
        Q.empiler(x)
    while not Q.est_vide():
        x = Q.depiler()
        pile.empiler(x)
    return i

def retourner(pile:Pile, i:int):
    Q = Pile()
    for i in range(i):
        Q.empiler(pile.depiler())
    for i in range(i):
        pile.empiler(Q.depiler())

def croissant(pile:Pile):
    for i in range(hauteur_pile(pile)):
        max = max_pile(pile, hauteur_pile(pile))
        retourner(pile, max)
        retourner(pile, hauteur_pile(pile))