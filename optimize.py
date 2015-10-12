#!/usr/bin/python
# -*-coding: utf-8 -*-

import numpy as np
from math import cos
from scipy.optimize import minimize
def myfunc1(x):
    return cos(x)*x
def myfunc2(x):
    return x*x*x/(5-x)

x0 = np.array([0, 4])
res = minimize(myfunc1, x0, method='powell', options={'xtol': 1e-8, 'disp': True})
dorez = res.x
