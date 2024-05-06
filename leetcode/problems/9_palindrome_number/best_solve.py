#!/usr/bin/env python3
# quite well?
def isPalindrome(n):
  if n < 0:
    return False

  r, temp = 0, n

  while temp != 0:
    digit = temp % 10
    print(f'digit: {digit}')
    r = r * 10 + digit
    print(f'r: {r}')
    temp //= 10
    print(f'temp: {temp}')
    print(f'in this loopie, is r == n? {r} == {n}')
    print('---')
  return r == n

print(isPalindrome(121))
