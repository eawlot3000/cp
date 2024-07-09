#!/usr/bin/env python3

# Read the dimensions of the matrix
m, n = map(int, input().split())

# Read the matrix
matrix = []
for _ in range(m):
  row = list(map(int, input().split()))
  matrix.append(row)
print(matrix)

# Initialize the sum of edge elements
edge_sum = 0

# Sum the first and last rows
for j in range(n):
  edge_sum += matrix[0][j]  # First row
  if m > 1:
    edge_sum += matrix[m-1][j]  # Last row

# Sum the first and last columns, excluding already counted corners
for i in range(1, m-1):
  edge_sum += matrix[i][0]  # First column
  if n > 1:
    edge_sum += matrix[i][n-1]  # Last column

# Print the result
print(edge_sum)






#input_lists = [list(map(int, line.split())) for line in input_data.strip().split('\n')]



'''
l = []

a = input().splitlines()
l.append(a)

print("".join(a))
print(l)
'''

'''
l = []

# Use a loop to read multiple lines of input
print("Enter your input (end with an empty line):")
while True:
  line = input()
  if line == "":
    break
  l.append(line)

# Split the input into lines
lines = l

# Initialize a list to hold the sums, with length of the longest line split
max_length = max(len(line.split()) for line in lines)
sums = [0] * max_length

# Iterate through each line
for line in lines:
  # Split the line into numbers
  numbers = list(map(int, line.split()))
  # Add each number to the corresponding position in the sums list
  for i, num in enumerate(numbers):
    sums[i] += num

# Output the result as required
print(sums)
'''

