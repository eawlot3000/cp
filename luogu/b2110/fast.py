#!/usr/bin/env python3
from collections import Counter

def first_unique_char(s):
  # Count occurrences of each character
  count = Counter(s)
  
  # Find the first character with count 1
  for char in s:
    if count[char] == 1:
      return char
  
  # If no unique character found, return "no"
  return "no"

# Example usage:
input_str = input().strip()
result = first_unique_char(input_str)
print(result)

