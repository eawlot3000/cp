#!/usr/bin/env python3
def era(n):
  is_prime = [True] * (n+1)
  for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
      for j in range(i*i, n+1, i):
        is_prime[j] = False
  li = [x for x in range(2, n+1) if is_prime[x]]
  return li

if __name__ == '__main__':
  a = 100
  for i in range(10000, 100000, 10):
    count_list = len(era(i))
    if count_list == 10001:
      print(era(i)[-1])
      break

