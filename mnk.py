from __future__ import division
from numpy import *
import numpy

def mult(A, X, k):
    R = A*X
    tmp = 0.
    for i in range(k):
        tmp = tmp + R[i]
    return tmp
inputFile = open("lab3.test.csv")
n = 18
k = n + 1
m = 2314
A = zeros((m + 1, k), dtype=float)
B1 = zeros(m + 1, dtype=float)
B2 = zeros(m + 1, dtype=float)
C1 = zeros(m + 1, dtype=float)
C2 = zeros(m + 1, dtype=float)
X10 = zeros(k, dtype=float)
X20 = zeros(k, dtype=float)
X1 = zeros(k, dtype=float)
X2 = zeros(k, dtype=float)
R1 = zeros(m + 1, dtype=float)
R2 = zeros(m + 1, dtype=float)
for i in range(m + 1):
    tmp = inputFile.readline().split(",")
    B1[i] = float(tmp[k])
    B2[i] = float(tmp[k+1])
    for j in range(k):
        A[i][j] = float(tmp[j])
#
X10 = numpy.linalg.lstsq(A, B1)
X20 = numpy.linalg.lstsq(A, B2)
for i in range(k):
    X1[i] = X10[0][i]
    X2[i] = X20[0][i]

counter1_1 = 0
counterKr_1 = 0
for i in range(m + 1):
    R1[i] = mult(A[i], X1, k)
    R2[i] = mult(A[i], X2, k)
    tmp = R1[i]
    tmp1 = C1[i]
    tmp2 = C2[i]
    if tmp >= 0.78:
        if tmp1 >= 0.78:
            counter1_1 += 1
    if tmp <= 0.78:
        if tmp1 <= 0.78:
            counter1_1 += 1
    if tmp >= 0.78:
        if tmp2 >= 0.78:
            counterKr_1 += 1
    if tmp <= 0.78:
        if tmp2 <= 0.78:
            counterKr_1 += 1
print "counter1_1 = " + str(m + 1 - counter1_1)
print "counterKr_1 = " + str(m + 1 - counterKr_1)

