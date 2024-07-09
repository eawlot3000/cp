#!/usr/bin/env python3
n = int(input())
ar1, ar2, c = [], [], 0
for i in range(n):
  a, b = map(int, input().split())
  ar1.append(a)
  ar2.append(b)
for i in range(len(ar2)):
  c += ar1.count(ar2[i])
print(c)

