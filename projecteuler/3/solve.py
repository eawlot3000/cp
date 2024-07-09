#!/usr/bin/env python3
def largest_prime_factor(n):
  i = 2
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
  return n

number = 600851475143
print(largest_prime_factor(number))
