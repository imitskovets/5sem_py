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
pdim = 30

for i in range(pdim+1):
    for j in range(pdim+1):
            for k in range(pdim+1):
                A = matrixcreator(i, j, k, pdim)
                if (np.linalg.norm(A, 1) <= 1.):
                    ax.scatter(i, j, k, zdir='k')

ax.legend()
ax.set_xlim3d(0, pdim)
ax.set_ylim3d(0, pdim)
ax.set_zlim3d(0, pdim)

plt.show()

