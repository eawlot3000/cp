#import numpy as np
from numpy import *

# draw the graph -> x
x = tile([0], (8,8))
n = int(input())
for i in range(n):
  w = str(input()).split()
  x[int(w[0])-1, int(w[1])-1] = int(w[-1])
#print('\n{}'.format(x))

# calculate 2 routes max
