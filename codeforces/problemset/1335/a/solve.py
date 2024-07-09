#!/usr/bin/env python3
n = int(input())
for i in range(n):
  ret = int(input())
  if ret%2:
    ret //= 2
  else:
    ret = int(ret/2 - 1)
  print(ret)
