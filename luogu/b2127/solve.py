#!/usr/bin/env python3

def is_perfect(num):
  if num < 2:
    return False
  sum_factors = 1
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      sum_factors += i
      if i != num // i:
        sum_factors += num // i
  return sum_factors == num

n = int(input())
for i in range(2, n + 1):
  if is_perfect(i):
    print(i)

