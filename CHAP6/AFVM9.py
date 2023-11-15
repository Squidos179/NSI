# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
line = ax.plot([1,2,3,4], [10,20,40,80], color='blue')
line2 = ax.plot([1,2,3,4], [20,30,50,90], color='red')
fig.show()
f = input()