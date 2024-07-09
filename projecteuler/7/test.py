#!/usr/bin/env python3
def find_some(l): # use function to find method of sieve of Eratosthenes first
  is_prime = [True] * (l)
  is_prime[0] = is_prime[1] = False

  for i in range(2, int(l ** 0.5) + 1):
    if is_prime[i]:
      for j in range(i * i, l, i):
        is_prime[j] = False

  return [i for i in range(2, l) if is_prime[i]]


if __name__ == '__main__':
  print(find_some(1000000)[10000]) # find 10001th prime number
