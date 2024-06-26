import doctest
from math import sqrt
import matplotlib.pyplot as plt 
from random import randint

L_POINTS = [(-0.9, -3.1), (-4.5, -6.8), (-9.5, 6.2), (6.8, 9.2), (5.8, 6.6),
            (3.7, 9.2), (-1.3, 0.1), (8.6, -1.9), (-8.4, 2.8), (1.7, -9.8),
            (-9.0, -5.6), (8.4, 6.6), (-6.1, -5.2), (-8.8, 3.4), (-7.0, -9.6),
            (-6.1, -3.1), (-3.5, 2.6), (4.7, -2.8), (-1.1, -9.3), (0.7, 6.6),
            (-9.7, -2.9), (-9.8, 8.1), (-7.3, 6.8), (-7.2, -6.5), (-2.5, -1.8),
            (-0.1, -0.3), (5.9, -3.9), (3.5, -1.1), (2.9, 7.9), (-8.1, 2.5)]

def distance(p1:tuple, p2:tuple)->float:
    """Fonction qui calcule la distance entre 2 points
    @params :
    - p1 : point 1 de type tuple avec 2 Ã©lÃ©ments correspondant aux coordonnÃ©es (x, y) du point
    - p2 : point 2 de type tuple avec 2 Ã©lÃ©ments correspondant aux coordonnÃ©es (x, y) du point
    @returns :
    type float
    >>> distance((2, 4),(5, 8))
    5.0
    """
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def plus_proches(points: list) -> (float, tuple, tuple):
    """Calcul la plus courte distance entre 2 points dans toute une liste
    suivant l' algorithme naif.
    @params :
    - points : de type list de tuples avec 2 Ã©lÃ©ments correspondant aux coordonnÃ©es (x, y) du point
    @returns :
    - dist_min : distance minimale de type float
    - p1 : 1er point de cette distance minimale de type tuple
    - p2 : 2e point de cette distance minimale de type tuple
    >>> plus_proches([(2,4), (33,33), (444,444),(5,8)])
    (5.0, (2, 4), (5, 8))
    >>> plus_proches(L_POINTS)
    (0.4242640687119289, (-8.4, 2.8), (-8.1, 2.5))
    """
    p1 = points[0]
    p2 = points[1]
    dist_min = distance(p1, p2)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist<dist_min:
                dist_min = dist
                p1 = points[i]
                p2 = points[j]
    return dist_min,p1,p2

def plus_proches_dpr(points: list) -> (float, tuple, tuple):
    """Calcul la plus courte distance entre 2 points dans toute une liste
    suivant l' algorithme diviser pour rÃ©gner.
    @params :
    - points : de type list de tuples avec 2 Ã©lÃ©ments correspondant aux coordonnÃ©es (x, y) du point
    @returns :
    - dist_min : distance minimale de type float
    - p1 : 1er point de cette distance minimale de type tuple
    - p2 : 2e point de cette distance minimale de type tuple
    >>> plus_proches_dpr([(2,4), (33,33), (444,444),(5,8)])
    (5.0, (2, 4), (5, 8))
    >>> plus_proches_dpr(L_POINTS)
    (0.4242640687119289, (-8.4, 2.8), (-8.1, 2.5))
    """
    #Etape 1 - Preliminaire
    px = points[:]
    py = points[:]
    px.sort(key =lambda p: [p[0]])
    py.sort(key =lambda p: [p[1]])
    #Etape 2 - Diviser
    if len(points) <= 3 : #A completer
        return plus_proches(points)
    else :
        #Etape 3 - Regner
        ax = px[:len(px)//2]
        bx = px[len(px)//2:]
        ay = py[:len(py)//2]
        by = py[len(py)//2:]
        delta, p1, p2 = min(plus_proches_dpr(ax), plus_proches_dpr(bx))
        #Etape 4 - Combiner
        x = px[len(px)//2]
        q = []
        for p in px :
            if distance(x, p) < delta:
                q.append(p)
        qy = q[:]
        qy.sort(key =lambda p: [p[1]])
        qy = [p for p in py if x - delta < p[0] < x + delta]
        if len(qy)>=2:
            min_comb = distance(qy[0], qy[1])
            p1_min, p2_min = qy[0], qy[1]
            for i in range(len(qy)-1):
                j = 1
                while j<=7 and i+j<len(qy):
                    #A completer
                    dist = distance(qy[i], qy[i + j])
                    if dist < min_comb:
                        min_comb = dist
                        p1_min, p2_min = qy[i], qy[i + j]
                    j+=1
            if delta>min_comb:
                delta = min_comb
                p1, p2 = p1_min, p2_min
    return delta, p1, p2

def graphique_ppdpr(nuage_points, p1=None, p2=None):
    list_x = [p[0] for p in nuage_points]
    list_y = [p[1] for p in nuage_points]
    plt.scatter(list_x,list_y, c='blue')
    if p1 and p2 :
        plt.scatter([p1[0], p2[0]],[p1[1], p2[1]], c='red')
    plt.show()

def genere_nuages_de_points(n=100):
    nuage_points = []
    for i in range(n):
        nuage_points.append((randint(-1000,1000)/100,randint(-1000,1000)/100))
    delta, p1, p2 = plus_proches_dpr(nuage_points)
    print(f"delta : {delta}, p1 : {p1}, p2 : {p2}")
    graphique_ppdpr(nuage_points, p1, p2)

doctest.testmod()
#print(plus_proches_dpr(L_POINTS))
#delta, p1, p2 = plus_proches_dpr(L_POINTS)
#graphique_ppdpr(L_POINTS, p1, p2)
#genere_nuages_de_points()
