#!/usr/bin/env python3
n = int(input())

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

prime_pairs = []
for p in range(2, n + 1):
  if is_prime(p) and is_prime(p + 2) and p + 2 <= n:
    prime_pairs.append((p, p + 2))

if not prime_pairs:
  print("empty")
else:
  for pair in prime_pairs:
    print(pair[0], pair[1])

