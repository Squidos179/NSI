def count_change(n, k ,pieces):
    cache = {}
    if n < 0:
        return 0
    if (n, k) in cache:
        return cache[n, k]
    if k == 0:
        v = 1
    else:
        v = count_change(n - pieces[k], k, pieces) + count_change(n, k -1, pieces)
    cache[n, k] = v
    return v

#En n*k car on converse tout les résultats précédants