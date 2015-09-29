#!/usr/bin/python
# -*- coding: utf-8 -*-

# input begin
try:
    inputFile = open("lab3.test.csv")
except IOError:
    print ("No file")
A  = zeros((2315, 33), dtype=float)
X1 = zeros(2315, dtype=float)
B = inputFile.readline().split(" ")
isItOk(size(B), n)
for i in range(n):
    B[i] = float(B[i])
    tmp = inputFile.readline().split(" ")
    isItOk(size(tmp), n)
    A[i] = tmp
inputFile.close()
# input end
