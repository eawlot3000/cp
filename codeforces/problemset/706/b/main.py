#!/usr/bin/env python3
n = int(input())
an = list(map(int, input().split()))
s = int(input())
ret = []
cnt = 0
for i in range(s):
  ret += [int(input())]
  for j in range(len(an)):
    if an[j] <= ret[i]:
      cnt += 1
  print(cnt)
  cnt = 0
