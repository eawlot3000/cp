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

def is_palindrome(x):
  return str(x) == str(x)[::-1]

def count_prime_palindromes(n):
  primes = sieve(n)
  count = 0
  for i in range(11, n + 1):
    if primes[i] and is_palindrome(i):
      count += 1
  return count

n = int(sys.stdin.read().strip())
print(count_prime_palindromes(n))

