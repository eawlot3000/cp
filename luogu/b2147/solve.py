#!/usr/bin/env python3
import math

x, n = map(float, input().split())
result = math.sqrt(1 + x)
for i in range(2, int(n) + 1):
  result = math.sqrt(i + result)

print(f"{result:.2f}")
