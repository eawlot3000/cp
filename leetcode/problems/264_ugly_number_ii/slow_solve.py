#!/usr/bin/env python3

# this is super slow and dumb

def nthUglyNumber(n):
  if n < 1:
    return -1

  a = [1]
  i = 2
  while len(a) < n:
    j = i
    while j%2 == 0:
      j //= 2
    while j%3 == 0:
      j //= 3
    while j%5 == 0:
      j //= 5
    if j == 1:
      a.append(i)
    i += 1
  return a[-1]

n = 100000
print(nthUglyNumber(n))  # 12
