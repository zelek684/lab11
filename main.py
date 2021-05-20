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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#zad1
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# t = np.linspace(0, 2*np.pi, 100)
# z = t
# x = np.sin(t)
# y = 2 * np.cos(t)
# ax.plot(x, y, z, label='zad1')
# ax.legend()
# plt.show()
#zad2
# np.random.seed(19680801)
# def randrange(n, vmin, vmax):
#     '''
#     Funkcja wspomagająca może tworzyć macierz losowych liczb o
#     kształcie(n, )
#     '''
#     return (vmax - vmin)*np.random.rand(n) + vmin
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
# for c, m, zlow, zhigh in [('r', '<', -50, -40), ('b', '*', -30, -20),
#                           ('g', '1', 10, 20), ('c', 's', 30, 40,),
#                           ('m', 'h', 50, 60)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel( 'X Label' )
# ax.set_ylabel( 'Y Label' )
# ax.set_zlabel( 'Z Label' )
# plt.savefig('zad2.png')
# plt.show()
#zad3
# fig = plt.figure(figsize=(16,9))
# ax = fig.add_subplot(1,3,1, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.hot, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
# ax = fig.add_subplot(1,3,2, projection='3d')
# surf1 = ax.plot_surface(X, Y, Z, cmap=cm.Pastel1, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf1,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
# ax = fig.add_subplot(1,3,3, projection='3d')
# surf1 = ax.plot_surface(X, Y, Z, cmap=cm.ocean, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf1,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
# plt.savefig('zad3.png')
# plt.show()
#zad4
# fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(231, projection='3d')
# ax2 = fig.add_subplot(232, projection='3d')
# ax3 = fig.add_subplot(233, projection='3d')
# ax4 = fig.add_subplot(234, projection='3d')
# ax5 = fig.add_subplot(235, projection='3d')
# colors = ['r', 'g', 'b', 'm', 'c', 'y']
# # fikcyjne dane
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ls = LightSource(azdeg=225.0, altdeg=45.0)
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres nie zacieniony')
# ax3.bar3d(x, y, bottom, width, depth, top, shade=True, lightsource=ls)
# ax4.bar3d(x, y, bottom, width, depth, top, color='r', alpha=0.1)
# for i in range(6):
#     ax5.bar3d(x, y, bottom, width, depth, top, color=colors[i], alpha=0.1)
# plt.savefig('zad4')
# plt.show()

#zad5
# fig = plt.figure(figsize=(16, 9))
# ax1 = fig.add_subplot(121, projection='3d')
#
# x = np.arange(-5, 5, 0.25)
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)
#
#
# surf1 = ax1.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax1.set_zlim(-1.01, 1.01)
# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# fig.colorbar(surf1, shrink=0.5, aspect=5)
# ax1 = fig.add_subplot(122, projection='3d')
# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)
# surf2 = ax1.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True)
# ax1.set_zlim(-1.01, 1.01)
# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# fig.colorbar(surf2, shrink=0.5, aspect=5)
# plt.savefig('wykres.png')
# plt.show()