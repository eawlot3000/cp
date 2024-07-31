#!/usr/bin/env python3
n = int(input())
primes = []
is_prime = [True] * (n + 1)

# Sieve of Eratosthenes to find all primes <= n
for p in range(2, n + 1):
  if is_prime[p]:
    primes.append(p)
    for multiple in range(p * p, n + 1, p):
      is_prime[multiple] = False

# Find the maximum product of two primes that sum to n
max_product = 0
prime_set = set(primes)

for p1 in primes:
  p2 = n - p1
  if p2 in prime_set:
    max_product = max(max_product, p1 * p2)

print(max_product)
