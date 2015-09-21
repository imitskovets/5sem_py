from datetime import datetime
from numpy import *
__author__ = 'van_mit'

n = int(raw_input("Enter system's rang n ="))
#for i in range(n):
A = empty((3, 3))
now1_1 = datetime.now().microsecond

now1_2 = datetime.now().microsecond
print now1_2 - now1_1
print n
print A
