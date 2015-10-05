from __future__ import division
from numpy import *

inputFile = open("lab3.test.csv")
outputFile = open("lab3.test2.csv", 'w')
n = 18
k = n + 1
m = 2314
A = zeros((m + 1, k), dtype=float)
X = zeros(m + 1, dtype=float)
for i in range(m):
    tmp = inputFile.readline().split(",")
    X[i] = tmp[k+1]
    for j in range(k):
        A[i][j] = tmp[j]
#
#
for i in range(m):
    outputFile.write(str(A[i]))
    outputFile.write(str(X[i]))
    outputFile.write('\n')
inputFile.close()
