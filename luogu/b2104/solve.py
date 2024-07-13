#!/usr/bin/env python3
n, m = map(int, input().split())

g1 = [list(map(int, input().split())) for _ in range(n)]
g2 = [list(map(int, input().split())) for _ in range(n)]

ret = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    ret[i][j] = g1[i][j] + g2[i][j]

for i in ret:
  print(' '.join(map(str, i)))


'''
print('\n\n----')
print(g1)
print('----')
print(g2)
print('----')
print(ret)
'''
