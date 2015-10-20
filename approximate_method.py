#!usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from datetime import datetime
from scipy.optimize import minimize

def func1(u):
    return ((u[0]**4 + np.sin(u[0]) - u[1])**2 + (u[0] - u[0]**2 - u[1]**2)**2)
def myGradient(x1, x2):
    result = np.array([[4*x1**3 + np.cos(x1), -1.0], [1.0 - 2*x1, - 2.0*x2]])
    return result
def func2(x1, x2):
    u = np.array([x1**4 + np.sin(x1) - x2, x1 - x1**2 - x2**2])
    return u

u0 = np.array([0.8, 0.8])
accuracy = 0.0000001

time_00 = datetime.now().microsecond
lib_solution = minimize(func1, u0, method = 'Nelder-Mead', options = {'xtol' : 1e-8, 'disp' : True})
time_01 = datetime.now().microsecond

time_10 = datetime.now().microsecond
n = 0
un = u0
while np.linalg.norm(func2(un[0], un[1])) > accuracy:
    un -= np.dot(np.linalg.inv(myGradient(un[0], un[1])), func2(un[0], un[1]))
    n += 1
time_11 = datetime.now().microsecond

print '\n'
print '             Library result:'
print 'Time:       '+str(time_01 - time_00)
print 'Iterations: '+str(lib_solution.nit)
print 'Solution:   '+str(lib_solution.x)
print '\n'
print '             My result:'
print 'Time:       '+str(time_11 - time_10)
print 'Iterations: '+str(n)
print 'Solution:   '+str(un)
