# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import sqrt
import timeit

def factorielClassique(n) :
    """
        >>> factorielClassique(5)
        120
        >>> factorielClassique(0)
        1
    """
    resultat = 1
    while n > 0:
        resultat *= n
        n -= 1
    return resultat

def factorielRecursive(n) :
    if n > 0 :
        return n*factorielRecursive(n-1)
    else :
        return 1
    
tps = []
tps2 = []
x = []

for i in range(900):
    print(i)
    x.append(i)
    tps.append(timeit.timeit(f"factorielClassique({i})", number = 1000, globals=globals()))
    tps2.append(timeit.timeit(f"factorielRecursive({i})", number = 1000, globals=globals()))

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
line = ax.plot(x, tps, color='blue')
line2 = ax.plot(x, tps2, color='red')
fig.show()
f = input()