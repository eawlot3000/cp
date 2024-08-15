#!/usr/bin/env python3
n, m = map(int, input().split())
lanterns = [0] * n
presses = [int(input()) for _ in range(m)]

for press in presses:
  x = press - 1
  lanterns[x] ^= 1
  lanterns[(x - 1) % n] ^= 1
  lanterns[(x + 1) % n] ^= 1

print(" ".join(map(str, lanterns)))
