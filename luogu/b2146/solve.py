#!/usr/bin/env python3
def hermite(n, x):
  if n == 0:
    return 1
  elif n == 1:
    return 2 * x
  else:
    h_0, h_1 = 1, 2 * x
    for i in range(2, n + 1):
      h_n = 2 * x * h_1 - 2 * (i - 1) * h_0
      h_0, h_1 = h_1, h_n
    return h_1

n, x = map(int, input().split())
print(hermite(n, x))

