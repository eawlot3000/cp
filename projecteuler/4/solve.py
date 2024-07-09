#!/usr/bin/env python3


#for i in range(10000, 998001):

def isPalindrome(n):
  return str(n) == str(n)[::-1]


def largest_palindrome():
  max_pal = 0
  for i in range(999, 99, -1):
    for j in range(i, 99, -1):
      product = i*j
      if isPalindrome(product) and product > max_pal:
        max_pal = product
  return max_pal

print(largest_palindrome())
