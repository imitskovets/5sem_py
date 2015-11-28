#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np

def func(x):
    return np.sin(x)

n = 1000
i_start = 0
i_end = 3.5

razb = np.linspace(i_start, i_end, n)
I = 0
for i in range(n-1):
    I += (razb[i+1] - razb[i]) * (func(razb[i]) + func(razb[i+1])) / 2
print I

