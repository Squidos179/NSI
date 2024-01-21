from __future__ import annotations
import bisect

class ArbreHuffman:

    def __init__(self, lettre, nbocc, g=None, d = None) -> None:
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d

    def est_feuille(self) -> bool:
        return self.gauche is None and self.droite is None
    
    def __lt__(self, other):
        return self.nbocc > other.nbocc
    
def parcours(arbre, chemin_en_cours, dico):
    if arbre is None:
        return
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        parcours(arbre.droite, chemin_en_cours + [1], dico)

def fusionne(gauche, droite) -> ArbreHuffman:
    nbocc_total = gauche.nbocc + droite.nbocc
    return ArbreHuffman(None, nbocc_total, gauche, droite)

def compte_occurences(texte) -> dict:
    occ = dict()
    for car in texte:
        if car not in occ:
            occ[car] = 0
        occ[car] += 1
    return occ

def construit_liste_arbres(texte) -> ArbreHuffman:
    dic_occurence = compte_occurences(texte)
    liste_arbres = []
    for lettre, occ in dic_occurence.items():
        liste_arbres.append(ArbreHuffman(lettre, occ))
    return liste_arbres

def codage_huffman(texte) -> dict:
    liste_arbres = construit_liste_arbres(texte)
    liste_arbres.sort()
    while len(liste_arbres) > 1:
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        bisect.insort(liste_arbres, new_arbre)
    arbre_huffman = liste_arbres.pop()
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico
        
with open("texte.txt") as f:
    texte = f.read()
print(codage_huffman(texte))