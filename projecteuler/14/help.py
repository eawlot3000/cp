#!/usr/bin/env python3

def collatz_sequence_length(n, known_lengths):
  original_n = n
  length = 0
  while n != 1 and n >= original_n:
    length += 1
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
  # Add the known lengths (if n has decreased below the original_n)
  length += known_lengths.get(n, 0)
  known_lengths[original_n] = length
  return length

def longest_collatz_sequence(limit):
  known_lengths = {1: 1}
  max_length = 0
  starting_number = 0
  for i in range(1, limit):
    length = collatz_sequence_length(i, known_lengths)
    if length > max_length:
      max_length = length
      starting_number = i
  return starting_number


print(longest_collatz_sequence(1000000))
