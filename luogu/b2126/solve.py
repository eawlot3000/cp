#!/usr/bin/env python3

k = int(input())
s = input()

def find_first_repeating_char(k, s):
  count = 1
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
      if count >= k:
        return s[i]
    else:
      count = 1
  return "No"

print(find_first_repeating_char(k, s))
