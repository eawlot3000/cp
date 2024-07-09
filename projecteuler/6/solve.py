#!/usr/bin/env python3
def sum_square_diff(n):
  sum_of_squares = n * (n+1) * (2*n+1) // 6

  sum_n = n * (n+1) // 2
  square_of_sum = sum_n ** 2

  return square_of_sum - sum_of_squares

n = 100
result = sum_square_diff(n)
print(result)
