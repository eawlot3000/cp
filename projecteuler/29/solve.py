#!/usr/bin/env python3

# two ranges
a = 100
b = 100
n = 0
ll = []

for i in range(2, a+1):
  for j in range(2, b+1):
    if i**j:
      n += 1
      ll += [i**j]
#print(ll)
print(len(set(ll)))
