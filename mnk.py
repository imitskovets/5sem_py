#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *

def mymult(A, X, k):
    R = A*X
    tmp = 0.
    for i in range(k):
        tmp = tmp + R[i]
    return tmp
def myfunc(x):
	#return exp(x)
	return x
inputFile = open("lab3.test.csv")
n = 18
k = n + 1
m = 2314
a = 1
w = myfunc(0.78)
A = zeros((m + 1, k + 1), dtype=float)
B1 = zeros(m + 1, dtype=float)
B2 = zeros(m + 1, dtype=float)
X10 = zeros(k + 1, dtype=float)
X20 = zeros(k + 1, dtype=float)
X1 = zeros(k + 1, dtype=float)
X2 = zeros(k + 1, dtype=float)
R1 = zeros(m + 1, dtype=float)
R2 = zeros(m + 1, dtype=float)
for i in range(m + 1):
    tmp = inputFile.readline().split(",")
    B1[i] = myfunc(float(tmp[k]))
    B2[i] = myfunc(float(tmp[k + 1]))
    A[i][k] = a
    for j in range(k):
        A[i][j] = float(tmp[j])
#
X10 = linalg.lstsq(A, B1)
X20 = linalg.lstsq(A, B2)
for i in range(k + 1):
    X1[i] = X10[0][i]
    X2[i] = X20[0][i]

counter11 = 0
counter1 = 0
counterKr = 0
counterKr1 = 0
for i in range(m + 1):
    R1[i] = mymult(A[i], X1, k+1)
    R2[i] = mymult(A[i], X2, k+1)
    tmp01 = R1[i]
    tmp02 = R2[i]
    tmp1 = B1[i]
    tmp2 = B2[i]
    if tmp01 >= w:
        if tmp1 >= w:
            counter1 += 1
    if tmp01 >= w:
        if tmp2 >= w:
            counter11 += 1
    if tmp02 <= w:
	if tmp1 <= w:
	    counterKr += 1
    if tmp02 <= w:
	if tmp2 <= w:
	    counterKr1 += 1
print "counter1 = " + str( counter1 + counter11)
print "counterKr = " + str( counterKr + counterKr1)

