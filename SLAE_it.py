#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import datetime
from numpy import *
__author__ = 'ivan_mitskovets'

def isItOk(x,rang):
    if x != rang:
        print "Wrong size!"
        exit(666)

# input begin
try:
    inputFile = open("inputSLAE.txt")
except IOError:
    print ("No file")
# n = int(raw_input("Enter system's rang n = "))
n = int(inputFile.readline())
A  = zeros((n, n), dtype=float)
X2 = zeros(n, dtype=float)
# B = raw_input("Enter vector B ").split(" ")
B = inputFile.readline().split(" ")
isItOk(size(B), n)
for i in range(n):
    B[i] = float(B[i])
    # tmp = raw_input("Enter line #" + str(i) + " ").split(" ")
    tmp = inputFile.readline().split(" ")
    isItOk(size(tmp), n)
    A[i] = tmp
inputFile.close()
# input end
now1_1 = datetime.now().microsecond
X0 = linalg.solve(A, B)
now1_2 = datetime.now().microsecond
A0 = A + zeros((n, n), dtype = float)
print "numpy result :"
print X0
print " numpy time = " + str(now1_2 - now1_1)
now2_1 = datetime.now().microsecond
w = 1.6
ww = float((1-w)/w)
# G 0 upright
G = A
for i in range(n-1):
	for j in range(i+1):
		G[j][i+1] = 0
C = A0 - G
D = zeros((n, n), dtype=float)
for i in range(n):
	D[i][i] = A0[i][i]
counter = 1000000
H = C + ww * D
K = G - ww * D
K1 = linalg.inv(K)
X  = zeros((counter, n), dtype=float)
Y  = ones(n, dtype=float) 
counter = 1
X[0]=Y 
untilIndex = 0.001
while (sum(abs(dot(A0,X[counter])-B)))>untilIndex:
	X[counter+1] = dot(K1,(B - dot(H,X[counter])))
	counter = counter +1
X2 = X[counter-1]
now2_2 = datetime.now().microsecond
print "my simple iteration result :"
print X2
print " my time = " + str(now2_2 - now2_1)
print "error :"
print str(abs(X2-X0))
print "                   deltaT = " + str(now1_2 - now1_1 - now2_2 + now2_1)

