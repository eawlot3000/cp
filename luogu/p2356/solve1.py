#!/usr/bin/env python3
n = int(input())
matrix = []

for _ in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)

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

