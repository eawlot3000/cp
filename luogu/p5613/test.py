# UNSOLVED !!!
import math
n,m,k = map(int,input().split())
time = 0
if k == 0:
  print('{}'.format(math.ceil(n/m)))
#first pt done
else:
  ret = [0] * k
  for i in range(k):
    ret[i] = int(input())
    for t in ret:
      rest = n-m
      time += 1
      if t == ret[i]:
        m += 1
      n = rest
      if rest<m:
        print('{}'.format(time+1))
