def ordre(G):
    return len(G)

def degre(G, s):
    return len(G[s])

def sommets_adjacents(G, s):
    if s in G:
        return G[s]
    return []

def lister_aretes(G):
    aretes = []
    for s in G:
        for t in G[s]:
            if (t, s) not in aretes:
                aretes.append((s, t))
    return aretes

def plus_grands_nombre_amis(G):
    max = 0
    for s in G:
        if degre(G, s) > max:
            max = degre(G, s)
    return max

def dic_to_matrice(G):
    sommets = ['a', 'b', 'c', 'd', 'e', 'f']
    n = len(sommets)
    matrice = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if sommets[j] in G[sommets[i]]:
                matrice[i][j] = 1
    return matrice

G = {}
G['a'] = ['b', 'c', 'd']
G ['b'] = ['a', 'd']
G['c'] = ['a', 'd', 'e']
G['d'] = ['a', 'b', 'c', 'e', 'f']
G['e'] = ['c', 'd', 'f']
G['f'] = ['d', 'e']

"""
print(G.keys())
print(G.values())
print(len(G))
print(G['e'])

for el in G.values():
    print(el)

for key in G.keys():
    print(key, G[key]) 

print(lister_aretes(G))
"""

feur = matrice(G)
for i in feur:
    print(i)