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
def getLineIndex(aUp, aDown, column):
    return float(A[aDown][column]/A[aUp][column])
def applyLineIndex(aUp, aDown, lineIndex): #todo /0 !!!!!!
    B[aDown] -= lineIndex * B[aUp]
    for i in range(n):
        A[aDown][i] -= lineIndex*A[aUp][i]
def setToZeroColumn(column):
    for i in range(n - 2, column, -1):
        aup = i
        adown = i + 1
        applyLineIndex(aup, adown, getLineIndex(aup, adown, column))
    if column != (n - 1):
        applyLineIndex(column, column + 1, getLineIndex(column, column + 1, column))
def setToZeroOnlyColumn(column):
    for i in range(column-1, -1, -1):
        index = A[i][column]/A[column][column]
        A[i][column] = 0
        B[i] -= index * B[column]
# input begin
try:
    inputFile = open("inputSLAE.txt")
except IOError:
    print ("No file")
# n = int(raw_input("Enter system's rang n = "))
n = int(inputFile.readline())
A  = zeros((n, n), dtype=float)
X1 = zeros(n, dtype=float)
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
A0 =A
print "numpy result :"
print X0
print " numpy time = " + str(now1_2 - now1_1)
now2_1 = datetime.now().microsecond
for i in range(n-1):
    setToZeroColumn(i)
for i in range(n):
    index = A[i][i]
    B[i] = B[i] / index
    for j in range(n):
        A[i][j] = A[i][j] / index
for i in range(n-1, -1, -1):
    setToZeroOnlyColumn(i)
    X1[i] = B[i]
now2_2 = datetime.now().microsecond
print "my gauss result :"
print X1
print " my time = " + str(now2_2 - now2_1)
print "error :"
print str(abs(X1-X0))
print "                   deltaT = " + str(now1_2 - now1_1 - now2_2 + now2_1)

