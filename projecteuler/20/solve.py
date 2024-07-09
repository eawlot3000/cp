#!/usr/bin/env python3
n = 1
for i in range(1, 101):
  n *= i
#print(n)
print(sum([int(i) for i in str(n)]))
