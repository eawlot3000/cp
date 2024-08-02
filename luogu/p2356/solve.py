#!/usr/bin/env python3
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
matrix = []
idx = 1

for i in range(n):
  row = list(map(int, data[idx:idx + n]))
  matrix.append(row)
  idx += n

row_sum = [0] * n
col_sum = [0] * n

for i in range(n):
  for j in range(n):
    if matrix[i][j] != 0:
      row_sum[i] += matrix[i][j]
      col_sum[j] += matrix[i][j]

max_kills = -1
for i in range(n):
  for j in range(n):
    if matrix[i][j] == 0:
      kills = row_sum[i] + col_sum[j]
      max_kills = max(max_kills, kills)

if max_kills == -1:
  print("Bad Game!")
else:
  print(max_kills)
