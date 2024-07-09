#!/usr/bin/env python3
n = int(input())
ret = []
for i in range(n):
  t = str(input())
  if t not in ret:
    print('\n')
    ret.append(t)
    print('OK')
  else:
    print(t + str(ret.count(t)))
    ret.append(t)
