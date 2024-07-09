#!/usr/bin/env python3

n = 2000000
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5)+1):
  if is_prime[i]:
    for j in range(i*i, n+1, i):
      is_prime[j] = False
print(sum([i for i in range(2, n) if is_prime[i]]))

#print(sum(ll))

'''
def seive(n):
  is_prime = [True] * (n+1)
  is_prime[0] = is_prime[1] = False
  for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
      for j in range(i*i, n+1, i):
        is_prime[j] = False
  return [i for i in range(2, n) if is_prime[i]]

if __name__ == '__main__':
  print(sum(seive(2000000)))
'''
