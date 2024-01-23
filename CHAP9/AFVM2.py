from __future__ import annotations

class Noeud :
    def __init__(self, valeur:int = None, noeud_suivant:Noeud = None) -> None:
        self.mNoeud_suivant = noeud_suivant
        self.mValeur = valeur

class Liste_abstraite :
    def __init__(self, noeud:Noeud = None) -> None:
        self.mNoeud = noeud

def vide() -> Liste_abstraite:
    return Liste_abstraite()

def est_vide(liste:Liste_abstraite) -> bool :
    return liste.mNoeud != None

def ajout_en_tete(noeudP:int, liste:Liste_abstraite) -> None:
    noeud = Noeud(noeudP)
    if est_vide(liste):
        liste.mNoeud = noeud
    else:
        noeud.mNoeud_suivant = liste.mNoeud
        liste.mNoeud = noeud

def suppr_en_tete(liste:Liste_abstraite) -> None:
    liste.mNoeud = liste.mNoeud.mNoeud_suivant

def cons(valeur, liste:Liste_abstraite) -> Liste_abstraite:
    return Liste_abstraite(Noeud(valeur, liste.mNoeud))

def compte(liste:Liste_abstraite) -> int:
    count = 0
    noeud = liste.mNoeud
    while noeud != None :
        count += 1
        noeud = noeud.mNoeud_suivant
    return count

L = vide()
ajout_en_tete(10, L)
ajout_en_tete(9, L)
ajout_en_tete(7, L)
L1 = vide()
L2 = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, L1))))))
suppr_en_tete(L2)
print(compte(L2))