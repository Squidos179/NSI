from __future__ import annotations

class Noeud :
    def __init__(self, valeur:int = None, noeud_suivant:Noeud = None) -> None:
        mNoeud_suivant = noeud_suivant
        mValeur = valeur

class Liste_abstraite :
    def __init__(self, noeud:Noeud = None) -> None:
        mNoeud = noeud

def vide() -> Liste_abstraite:
    return Liste_abstraite()

def est_vide(liste:Liste_abstraite) -> bool :
    return liste.mNoeud != None

def ajout_en_tete(noeud:int, liste:Liste_abstraite) -> None:
    if est_vide(liste):
        liste.mNoeud = Noeud(noeud, None)
    else:
        noeud.mNoeud_suivant = liste.mNoeud
        liste.mNoeud = noeud

def suppr_en_tete(liste:Liste_abstraite, noeud:Noeud) -> None:
    liste.mNoeud = liste.mNoeud.mNoeud_suivant

def cons(valeur, liste:Liste_abstraite) -> Liste_abstraite:
    return Liste_abstraite(Noeud(valeur, liste.mNoeud))

def compte(liste:Liste_abstraite) -> int:
    count = 0
    noeud = liste.mNoeud
    while noeud != None :
        count += 1
        noeud = noeud.mNoeud_suivant

L = vide()
ajout_en_tete(10, L)
ajout_en_tete(9, L)
ajout_en_tete(7, L)
L1 = vide()
L2 = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, L1))))))