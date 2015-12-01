#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import random as random

def func1(x, n):
    rez = 0
    for i in range(n):
        rez += x[i]**2
    return rez

def func2(x):
    return np.exp(-x**2)


number_of_points = 10000000
n = 2
total_volume = 2**n
hit_number = 0

for i in range(number_of_points):
    x = []
    for j in range(n):
        x.append(random.uniform(0, 1))
    if 1 > func1(x, n)**2:
        hit_number += 1
volume = total_volume * hit_number / number_of_points
print 'Volume of ' + str(n) + ' dimension sphere = ' + str(volume)
volume = 0
hit_number = 0
for i in range(number_of_points):
    x = []
    y = []
    for j in range(n):
        x.append(random.uniform(0, 1))
        y.append(func2(x[j]))
    if 1 > func1(y, n):
        hit_number += 1
volume = total_volume * hit_number / number_of_points
print 'Integral of ' + str(n) + ' dimension gauss = ' + str(volume)
volume = 0
hit_number = 0
r = 0.1
for i in range(number_of_points):
    x = []
    for j in range(n):
        x.append(random.uniform(0, 1))
    if (1 > func1(x, n)**2) and (r**2 < func1(x, n)**2):
        hit_number += 1
volume = total_volume * hit_number / number_of_points
print 'Volume of ' + str(n) + ' dimension sphere with hole(r = ' + str(r) + ') = ' + str(volume)