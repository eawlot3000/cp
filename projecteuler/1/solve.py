#!/usr/bin/env python3
n = int(input())
ret = 0
for i in range(1, n):
  if i % 3 == 0 or i % 5 == 0:
    ret += i
print(ret)
