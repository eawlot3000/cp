# -- test --
from numpy import *
x = tile([0], (3,3))
#n = int(input())
n = 3
x[0,1] = 3
x[0,2] = 2
x[2,2] = 8
'''
for i in range(n):
  w = str(input()).split()
  #print(type(w[0]))
  x[int(w[0])-1, int(w[1])-1] = int(w[-1])
  '''
print('\n{}\n'.format(x))
'''
[[0 3 2]
 [0 0 0]
 [0 0 8]]
'''
arr = 0
for i in range(3):
  for j in range(3):
    arr += int(x[i,j])
    print(x[i,j])
ptrint(arr)




