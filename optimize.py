#!/usr/bin/python
# -*-coding: utf-8 -*-

import numpy as np
from math import cos
from scipy.optimize import minimize
def myf(x):
    return (x[0]**2-2*x[1])**2+(x[1]-cos(x[0]))**2

x0 = np.array([0,4])
res = minimize(myf, x0, method='powell', options={'xtol': 1e-8, 'disp':True})
dorez = res.x
