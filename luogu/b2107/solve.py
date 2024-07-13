#!/usr/bin/env python3
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
ret = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    ret[j][n-i-1] = g[i][j]
    #ret[i][j] = g[m-j-1][i]
#print(ret)
for i in ret:
  print(' '.join(map(str, i)))
