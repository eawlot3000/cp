#!/usr/bin/env python3
n = int(input())
matrix = [[0] * n for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0
x, y = 0, 0
for i in range(1, n*n+1):
  matrix[x][y] = i
  dx, dy = directions[dir_idx]
  new_x, new_y = x+dx, y+dy
  if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or matrix[new_x][new_y] != 0:
    dir_idx = (dir_idx + 1) % 4
    dx, dy = directions[dir_idx]
    new_x, new_y = x+dx, y+dy
  x, y = new_x, new_y
for i in range(n):
  for j in range(n):
    print('{:3d}'.format(matrix[i][j]), end='')
  print()
