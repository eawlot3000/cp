#!/usr/bin/env python3
n, t = map(int, input().split())
q = list(input())
for _ in range(t):
  i = 0
  while i < n-1:
    if q[i] == 'B' and q[i+1] == 'G':
      q[i], q[i+1] = q[i+1], q[i]
      i += 2
    else:
      i += 1
print("".join(q))
