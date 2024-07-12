#!/usr/bin/env python3

# this is way faster and got approved
# even for python3

# Read the 5x5 matrix
grid = [list(map(int, input().split())) for _ in range(5)]

# Step 1: Find the maximum values and their column indices in each row
row_maxes = [(max(row), row.index(max(row))) for row in grid]

# Step 2: Find the minimum values in each column
col_mins = [min(grid[row][col] for row in range(5)) for col in range(5)]

# Step 3: Check for saddle points
found = False
for i, (row_max, col_index) in enumerate(row_maxes):
  if row_max == col_mins[col_index]:
    print(f"{i+1} {col_index+1} {row_max}")
    found = True
    break

if not found:
  print("not found")

