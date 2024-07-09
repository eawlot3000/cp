#!/usr/bin/env python3
n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

max_idx = heights.index(max_height)
min_idx = heights[::-1].index(min_height)

if max_idx > n - 1 - min_idx:
    seconds = max_idx + min_idx - 1
else:
    seconds = max_idx + min_idx

print(seconds)

