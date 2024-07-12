#!/usr/bin/env python3
for i in range(5):
  row_max = max(grid[i])
  col_index = grid[i].index(row_max)

  if all(row_max <= grid[j][col_index] for j in range(5)):
    print(f"{i+1} {col_index+1} {row_max}")
    break
else:
  print('not found')

'''
grid = []
for _ in range(5):
  grid.append(list(map(int, input().split())))
print(grid)
'''


''' print them all out
for i in range(5):
  for j in range(5):
    print(grid[i][j], end=' ')
  print('')
'''
