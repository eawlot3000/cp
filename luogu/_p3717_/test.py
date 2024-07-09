import math
import numpy as np
n,m,r = map(int, input().split())
ret = [][] #TODO: how to solve this bitch? a more complex python list
for t in range(m):
  x,y = map(int, input().split())
  for i in range(n):
    for j in range(n):
      dd = math.sqrt((x-i)*(x-i)+(y-j)*(y-j))
      if dd <= r:
        ret[i][j] = 1
for i in range(n):
  for j in range(n):
    if ret[i][j] == 1:
      count += 1
print(count)
