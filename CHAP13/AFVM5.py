from functools import lru_cache

@lru_cache
def rendu_monnaie_rec(liste_pieces, X):
    if X==0:
        return 0
    else:
        mini = 1000
    for piece in liste_pieces:
        if piece <=X:
            nb = 1 + rendu_monnaie_rec(liste_pieces,X-piece)
            if nb <mini:
                mini = nb
    return mini

pieces = (2, 5, 10, 50, 100)

def rendu_monnaie_mem(liste_pieces,X):
    mem = [0]*(X+1)
    return rendu_monnaie_mem_c(liste_pieces, X, mem)

def rendu_monnaie_mem_c(liste_pieces, X, m):
    if X == 0:
        return 0    
    elif m[X]> 0:
        return m[X]
    else:
        mini = 1000
        for piece in liste_pieces:
            if piece <=X:
                nb = 1 + rendu_monnaie_mem_c(liste_pieces, X-piece, m)
                if nb < mini:
                    mini =nb
                    m[X] = mini
    return mini

print(rendu_monnaie_mem(pieces, 171))