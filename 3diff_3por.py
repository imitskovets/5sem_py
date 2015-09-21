#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import math
import numpy
from numpy import *
import matplotlib.pyplot as plt

numberOfPoints = 10000	
hMin = 0.00001		
hMax = 1
x0 = 1.57

def func(x):
	return exp(x)
def funcd(x):
	return exp(x)
def f(z):
	return (((-1/4)*func(x0-2*z)+(-1/4)*func(x0-z)+(5/2)*func(x0)+
		(-7/2)*func(x0+z)+(7/4)*func(x0+2*z)+(-1/4)*func(x0+3*z))/(z*z*z))

hList = linspace(hMin, hMax, numberOfPoints)
hLogList = log(hList)
yList = abs((funcd(x0)-f(hList))/(funcd(x0)))
yLogList = log(yList)

print "Min error (x0) = ", min(yList)*100, "%"
miny = min(yLogList)				
for i in range(numberOfPoints):			 
	if yLogList[i] == miny:
		print  "With h (x0) = ", hList[i]

plt.plot(hLogList, yLogList)

plt.grid(True)
plt.show()
