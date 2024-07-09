#!/usr/bin/env python3
# Puzzles
# https://codeforces.com/problemset/problem/337/A
n, m = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
#print('->', p)

min_diff = float('inf') # the largest float number

for i in range(n - 1, m):
  print(p[i], p[i - n + 1])
  min_diff = min(min_diff, p[i] - p[i - n + 1])

print(min_diff)
