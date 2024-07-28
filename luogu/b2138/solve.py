#!/usr/bin/env python3
def max_prime_factor(num):
  if num <= 1:
    return None
  if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    return num
  max_factor = 1
  for i in range(2, int(num**0.5) + 1):
    while num % i == 0:
      max_factor = i
      num //= i
  if num > 1:
    max_factor = num
  return max_factor

def max_prime_factors_sequence(m, n):
  return [max_prime_factor(i) for i in range(m, n + 1)]

m, n = map(int, input().split())
result = max_prime_factors_sequence(m, n)
print(','.join(map(str, result)))


