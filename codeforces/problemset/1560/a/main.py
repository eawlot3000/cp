#!/usr/bin/env python3
ret = []
for i in range(1,2000):
  if i%3==0 or str(i)[-1]=='3':
    continue
  else:
    ret.append(i) 
n = int(input())
for j in range(n):
  an = int(input())
  print(ret[an-1])
