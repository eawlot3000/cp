#!/usr/bin/env python3

n = 1001
a, add, summ = 1, 2, 0
current = a
while True:
  for i in range(4):
    summ += current
    print(current)
    current += add
    if current > n**2:
      break
  if current > n**2:
    break
  add += 2

# you can get rid of print(current)
print(summ)
