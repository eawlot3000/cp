#!/usr/bin/env python3
def count_ab_classes(n):
  a_count = 0
  b_count = 0
  for i in range(1, n + 1):
    bin_str = bin(i)[2:]
    ones = bin_str.count('1')
    zeros = bin_str.count('0')
    (a_count, b_count) = (a_count + 1, b_count) if ones > zeros else (a_count, b_count + 1)

    '''
    if ones > zeros:
      a_count += 1
    else:
      b_count += 1
    '''

  return a_count, b_count

# Input example
n = int(input())
a_count, b_count = count_ab_classes(n)
print(a_count, b_count)

