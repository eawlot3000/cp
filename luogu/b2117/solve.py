#!/usr/bin/env python3
n = int(input())
for i in range(n):
  s = str(input()).lower()
  print(s[0].upper() + s[1:])
