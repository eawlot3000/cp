#!/usr/bin/env python3

def fac(n): # factorial # https://zh.wikipedia.org/wiki/%E9%9A%8E%E4%B9%98
  a = 1
  for i in range(1, n+1):
    a *= i
  return a

#paths = fac(40) // (fac(40-20))
paths = fac(40) // (fac(20) * fac(40-20))
print(paths)
