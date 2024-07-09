#!/usr/bin/env python3
def cal(n):
  c = 0
  for i in range(1, n+2):
    b = i
    a = n-i
    if a > b:
      c += 1
  return c

n = int(input())
ret = []
for i in range(n):
  ret += [int(input())]
  print(cal(ret[i]))


