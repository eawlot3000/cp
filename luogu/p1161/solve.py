#!/usr/bin/env python3
#from collections import Counter as C

# to improve here:
#from math import floor
#from collections import defaultdict


# use a dict instead of list
lights = {}

n = int(input())
l = []
for i in range(n):
  a, b = map(float, input().split())
  a, b = a, int(b)

  for j in range(1, b+1):
    # use int. or use from math import floor 
    idx = int(a*j)
    if idx not in lights:
      lights[idx] = 0
    lights[idx] += 1
      

for k, v in lights.items():
  if v % 2 != 0:
    print(k)
    break




  '''
  for j in range(b): # do not use this list since it could be very large
    l += [float(a*j)]
  '''
#print(l)
print('\n========\n', C(lights), '\n========\n')
