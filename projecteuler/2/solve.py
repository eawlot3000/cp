#!/usr/bin/env python3
def even_f(limit):
  a, b, t = 1, 2, 0 
  while b <= limit:
    if b%2 == 0:
      t += b
    a, b = b, a+b
  return t

print(even_f(4000000)
