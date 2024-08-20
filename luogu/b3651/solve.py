#!/usr/bin/env python3
# Read the input values
n, k = map(int, input().split())
a = list(map(int, input().split()))
a[k-1] = -a[k-1]
result = sum(a)
print(result)

