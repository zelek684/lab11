import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *

#zadanie1

fig = plt.figure()
ax = fig.gca(projection='3d')


z = np.linspace(0, 2 * np.pi)
x = np.sin(z)
y = 2 * np.cos(z)

ax.plot(z, x, y)
plt.show()

#zadanie2

fig = plt.figure()
ax = fig.gca(projection='3d')

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n)+vmin

for c, m in [('r', 'o'), ('b', '^'), ('g', 'P'), ('m','*'), ('y','s')]:
    s1 = randrange(100, 20, 30)
    s2 = randrange(100, 30, 40)
    s3 = randrange(100, 40, 50)
    s4 = randrange(100, 50, 60)
    s5 = randrange(100, 60, 70)
    ax.scatter(s1, s2, s3, s4, s5, c=c, marker=m)

ax.set_xlabel('x Label')
ax.set_ylabel('y Label')
ax.set_zlabel('z Label')

plt.show()
