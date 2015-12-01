#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import math as math
from sympy import *


def func(x):
    return x*(10*x+1)*(10*x+2)
    #return np.sin(x)

#n = 1000
h = 0.1
e = 0.0001
i_start = 0
i_end = 1
x = symbols('x')
I = integrate(x*(10*x+1)*(10*x+2), (x , i_start, i_end))
print 'sympy I = ' + str(I)

n = int(math.ceil((i_end - i_start) // h ) + 1)
razb = np.linspace(i_start, i_end, n)
I1 = 0.0
for i in range(n-1):
    I1 += (razb[i+1] - razb[i]) * (func(razb[i]) + func(razb[i+1])) / 2
print 'My trapeze method(const h = ' + str(h) + ')   :            I = ' + str(I1)

accuracy = 1.0
hi = 0.1
I2 = 0.0
Itmp = 0.0
while (accuracy > e):
    Itmp = I2
    I2 = 0.0
    n = int(math.ceil((i_end - i_start) // hi ) + 1)
    razb2 = np.linspace(i_start, i_end, n)
    for i in range(n-1):
        I2 += (razb2[i+1] - razb2[i]) * (func(razb2[i]) + func(razb2[i+1])) / 2
    accuracy = math.fabs(I2 - Itmp)
    print I2
    hi = hi / 10

print 'My trapeze method(const e = ' + str(e) + ') :            I = ' + str(I2) + '                 with h = ' + str(hi)
