#!/usr/bin/env python3


def cal(a):
  s = 1
  for i in range(1, int(a)+1):
    s *= i
  return s


n = '1'
s = 0
ll = []
while True:
  for i in range(len(n)):
    s += cal(n[i])
  if s == int(n):
    ll.append(s)
  n = int(n)
  n += 1
  n = str(n)
  print(n, ll)




