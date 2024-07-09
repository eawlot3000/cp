#!/usr/bin/env python3
def is_prime(n):
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def sum_primes_below_n(n):
  return sum([x for x in range(2, n) if is_prime(x)])

# Example usage:
n = 2000000  # You can change this number to the desired limit
result = sum_primes_below_n(n)
print(f"The sum of prime numbers below {n} is: {result}")

