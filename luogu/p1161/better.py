#!/usr/bin/env python3
from math import floor
from collections import defaultdict

n = int(input())
lights = defaultdict(int)

for _ in range(n):
  a, b = map(float, input().split())
  a = a
  b = int(b)
  for j in range(1, b + 1):
    idx = floor(a * j)
    lights[idx] += 1

for key, value in lights.items():
  if value % 2 != 0:
    print(key)
    break
