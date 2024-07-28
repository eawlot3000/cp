#!/usr/bin/env python3
def sum_n(n):
  return 1 if n == 1 else n + sum_n(n - 1)

n = int(input())
print(sum_n(n))



''' should be right, but cannot pass it
# short
n = int(input())
print((lambda n: (lambda f, x: f(f, x))(lambda f, x: 1 if x == 1 else x + f(f, x), n))(n))
'''
