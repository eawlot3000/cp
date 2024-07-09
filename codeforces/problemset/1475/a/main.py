#!/usr/bin/env python3
n = int(input())
ret = []
for i in range(n):
  ai = int(input())
  for j in range(1, ai):
    if ai/j is int and ai % j == 1:
      break
print(ret)
