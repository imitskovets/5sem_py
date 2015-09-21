#!/usr/bin/python
# -*-coding: utf-8 -*-

import math
from numpy import *
import matplotlib.pyplot as plt

#matplotlib.use('Agg')		# do not show figure in window
def func1 (x):    		# define function1 
	return exp(x)
label1 = 'exp^x'		# define function1 label
def func2 (x):			# define function2			
	return (exp(x))/2
label2 = '(exp^x)/2'		# define function2 label

x = linspace(0 , 10 , 100 )	# take 100 dots from 0 to 10
y1 = func1 (x)			# calculate y1 for every x
y2 = func2 (x)			# calculate y2 for every x

plt.plot(x, y1,
	'g-', label=label1 )	# build plot for func1
plt.plot(x, y2,
	'r-', label=label2 )	# bild plot for func2
				# b,c,k,g,r,w,y,m	-	--	-.	:	^	o-	+	x	|
#plt.axis([0, 10, 0, 1000000]) 	# [xmin, xmax, ymin, ymax]
plt.xlabel('x')   		# lable for x1
plt.ylabel('y')   		# lable for x2
plt.title(
	'My first normal plot') # plot's name
plt.legend(loc='upper left')    # build legend
plt.grid(True)			# build grid
plt.show()			# show our plot
#plt.savefig('name_of_plot.png',
#		dpi=200)	# save sa ...
