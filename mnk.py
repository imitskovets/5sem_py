from __future__ import division
from numpy import *
import numpy

inputFile = open("lab3.test.csv")
#outputFile = open("lab3.test2.csv", 'w')
n = 18
k = n + 1
m = 2314
A = zeros((m + 1, k), dtype=float)
B1 = zeros(m + 1, dtype=float)
B2 = zeros(m + 1, dtype=float)
C1 = zeros(m + 1, dtype=float)
C2 = zeros(m + 1, dtype=float)
X1 = zeros(k, dtype=float)
X2 = zeros(k, dtype=float)
for i in range(m + 1):
    tmp = inputFile.readline().split(",")
    B1[i] = int(tmp[k])
    B2[i] = int(tmp[k+1])
    for j in range(k):
        A[i][j] = int(tmp[j])
#
X1 = numpy.linalg.lstsq(A, B1)
X2 = numpy.linalg.lstsq(A, B2)
#
#for i in range(m + 1):
    #outputFile.write(str(A[i]) + str(B1[i]) + str(B2[i]) + '\n')
inputFile.close()
