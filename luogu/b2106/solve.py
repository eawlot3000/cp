#!/usr/bin/env python3
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
#print(g)

ret = [[0] * n for _ in range(m)]
#ret = [[0] * m for _ in range(n)] # u cant fuck this shit up aint u?
#print(ret)

for i in range(n):
  for j in range(m):
    ret[j][i] = g[i][j]
    #ret[i][j] = g[j][i]
#print(ret)

for i in ret:
  print(' '.join(map(str, i)))


'''
for i in range(len(g)):
  print(type(g[i]))
  print(i)
  print(' '.join(map(str, i)))
'''
