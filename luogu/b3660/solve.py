#!/usr/bin/env python3
T = int(input())
results = []
for _ in range(T):
  n = int(input())
  cards = list(map(int, input().split()))
  if 0 in cards:
    results.append("yes")
  else:
    results.append("no")
print("\n".join(results))
