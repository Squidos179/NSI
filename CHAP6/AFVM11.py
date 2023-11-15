# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import sqrt
import timeit

def fib(n):
    if n == 0:
        return  0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

tps = []
x = []

for i in range(30):
    print(i)
    x.append(i)
    tps.append(timeit.timeit(f"fib({i})", number = 1, globals=globals()))

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
line = ax.plot(x, tps, color='blue')
fig.show()
f = input()