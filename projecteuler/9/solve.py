#!/usr/bin/env python3

def find():
  for a in range(1, 333):
    for b in range(a+1, 500):
      c = 1000-a-b
      if a**2 + b**2 == c**2:
        return a, b, c, a*b*c

print(find())
