#!/usr/bin/env python3
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# Use a list comprehension to create the rotated matrix
ret = [[g[i][j] for i in range(n-1, -1, -1)] for j in range(m)]

# Print the rotated matrix
for row in ret:
  print(' '.join(map(str, row)))

