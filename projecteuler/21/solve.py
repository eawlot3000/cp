#!/usr/bin/env python3
# question itself: https://projecteuler.net/problem=21 itself is very vague, i did added twice at the end and got wrong

def cal_sum(n):
  ll = []
  for i in range(1, n//2+1):
    if n % i == 0:
      ll.append(i)
  return sum(ll)

s = 0
for i in range(1, 10001):
  j = cal_sum(i)
  if cal_sum(i) == j and cal_sum(j) == i and i != j:
    #t = i + j # t += i (or j, once)
    s += i # (or +j once)
print(s) # or print(s//2) if you add i+j to t per time
