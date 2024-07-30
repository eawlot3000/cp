#!/usr/bin/env python3
import sys
import math

def sieve(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = is_prime[1] = False
  for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
      for j in range(i * i, n + 1, i):
        is_prime[j] = False
  return is_prime

def count_primes_between(x, y):
  x, y = min(x, y), max(x, y)
  primes = sieve(y)
  return sum(primes[x:y + 1])

x, y = map(int, sys.stdin.read().strip().split())
print(count_primes_between(x, y))
