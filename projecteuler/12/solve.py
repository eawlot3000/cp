#!/usr/bin/env python3
import math

def tri_nums(n): # calculate the nth triangle number (last num)
  return n * (n+1) // 2

def count_divisors(n):
  c = 0 # count all divisors
  sqrt_n = int(math.sqrt(n))
  for i in range(1, sqrt_n+1):
    if n % i == 0:
      c += 2
  if sqrt_n ** 2 == n:
    c -= 1
  return c

def find_tri_num(div):
  n = 1
  while True:
    tri_num = tri_nums(n)
    if count_divisors(tri_num) > div:
      return tri_num
    n += 1

if __name__ == '__main__':
  print(find_tri_num(500))
