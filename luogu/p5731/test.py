#!/usr/bin/env python3
n = int(input())

matrix = [[0] * n for _ in range(n)] # 初始化一个 n×n 的方阵

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 定义蛇形矩阵的四个方向

direction_idx = 0 # 初始方向为向右，从左上角开始填充矩阵
x, y = 0, 0

# 举个例子，当 $n=4$ 时，首先初始化一个 $4\times 4$ 的方阵 matrix，然后从左上角开始填充矩阵。初始方向为向右，第一个数字为 $1$，填充在位置 $(0,0)$。然后向右移动一位，填充数字 $2$，填充在位置 $(0,1)$。再向右移动一位，填充数字 $3$，填充在位置 $(0,2)$。此时，已经填充了第一行的所有数字，需要向下移动一行，同时方向也要变为向下。继续按照这个规律填充数字，直到所有位置都被填充完为止。

for i in range(1, n * n + 1): # 填充矩阵
  matrix[x][y] = i
  dx, dy = directions[direction_idx]
  new_x, new_y = x + dx, y + dy
  if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or matrix[new_x][new_y] != 0:
    # 如果超出边界或者下一个位置已经被填充过，则换一个方向
    direction_idx = (direction_idx + 1) % 4
    dx, dy = directions[direction_idx]
    new_x, new_y = x + dx, y + dy
  x, y = new_x, new_y

# 输出矩阵
for i in range(n):
  for j in range(n):
    print('{:3d}'.format(matrix[i][j]), end='')
  print()
