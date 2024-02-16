lab2 = [[1, 1, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 3, 1]]


def est_valide(i, j, n, m):
    return n > i >= 0 and m > j >= 0

def voisines(i, j ,lab):
    list = []
    for k in range(i - 1, i + 2):
        for p in range(j - 1, j + 2):
            if est_valide(k, p, len(lab), len(lab[0])) and k != i and p !=j:
                if lab[k][p] == 0 or lab[k][p] == 3:
                    list.append((k, p))
    return list

def resolution(lab):
    chemin = []
    sucess = False
    for i in range(len(lab)):
        for p in range(len(lab[i])):
            if lab[p][i] == 2:
                chemin.append((p, i))
    pos = chemin[0]
    print(pos)
    while sucess != True:
        print(voisines(pos[0], pos[1], lab))
        pos = voisines(pos[0], pos[1], lab)[0]
        chemin.append(pos)
        if lab[pos[0]][pos[1]] == 0:
            lab[pos[0]][pos[1]] = 4
        if lab[pos[0]][pos[1]] == 3:
            sucess = True
    return chemin

print(voisines(0, 1, lab2))
print(resolution(lab2))