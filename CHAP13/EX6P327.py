from functools import lru_cache

def nb_rendus(n, pieces):
    if n < 0 or len(pieces) == 0:
        return 0
    if n > 0:
        return nb_rendus(n, pieces[:-1]) + nb_rendus(n-pieces[-1], pieces)
    return 1

print(nb_rendus(120, [2, 3, 7, 23, 47]))
print(nb_rendus(3000, [1, 5, 10, 25, 50]))