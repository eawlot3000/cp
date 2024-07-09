#!/usr/bin/env python3
#n = int(input())
n = 125
c = 0

while n>0:
  if n >= 100:
    n //= 100
    c += 1
  elif 20 < n < 100:
    n //= 20
    c += 1
  elif 10 < n < 20:
    n //= 10
    c += 1
  elif 5 < n < 10:
    n //= 5
    c += 1
  elif 1 < n <= 5:
    n //= 1
    c += 1
  elif n == 1:
    c += 1
print(c)

  
