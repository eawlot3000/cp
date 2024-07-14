#!/usr/bin/env python3
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# this line important
o = [row[:] for row in g]

for i in range(1, n-1):
  for j in range(1, m-1):
    t = g[i][j] + g[i-1][j] + g[i+1][j] + g[i][j-1] + g[i][j+1]
    #print(t, end=' ')
    o[i][j] = round(t/5)

for i in o:
  print(' '.join(map(str, i)))
