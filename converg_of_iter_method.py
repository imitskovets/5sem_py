#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def matrixcreator (a, b, c, n):
    A = zeros((n, n), dtype=float)
    for i in range(n):
        A[i][i] = a
    for i in range(n-1):
        A[i][i+1] = b
        A[i+1][i] = b
    for i in range(n-2):
        A[i][i+2] = c
        A[i+2][i] = c
    return A
A = matrixcreator(1, 2, 3, 6)

fig = plt.figure()
ax = fig.gca(projection='3d')
pdimr = 1
pdiml = 1
d = 0.1

for i in np.arange(-pdiml, pdimr, d):
    for j in np.arange(-pdiml, pdimr, d):
            for k in np.arange(-pdiml, pdimr, d):
                A = matrixcreator(i, j, k, pdimr+pdiml)
                if (np.linalg.norm(A, 1) <= 1.):
                    ax.scatter(i, j, k, zdir='k')

ax.legend()
ax.set_xlim3d(-pdiml, pdimr)
ax.set_ylim3d(-pdiml, pdimr)
ax.set_zlim3d(-pdiml, pdimr)

plt.show()

