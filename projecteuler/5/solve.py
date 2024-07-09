#!/usr/bin/env python3

def is_divisible(n):
  for i in range(1, 21):
    if n % i != 0:
      return False
  return True

def smallest_multiple(n):
  for i in range(100000, 1000000000):
    if is_divisible(i):
      return i
print(smallest_multiple())
