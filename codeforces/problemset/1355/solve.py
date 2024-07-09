#!/usr/bin/env python3
cases = int(input())
for i in range(cases):
  can = int(input())
  print(int(can//2) if can%2==0 else int(can/2-1))
  if can%2:
  else:
    print(int(can/2-1))

'''
now this is only a test
cases = int(input())
for i in range(cases):
  sum = 0 
  candies = int(input())
  b = 0
  for j in range(candies):
    a = candies - b
    if a>b:
      b += 1
      sum += 1
  print(sum-1)
'''
