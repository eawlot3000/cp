#!/usr/bin/env python3

# wait this faster?
n = int(input())
for _ in range(n):
  s = input()
  if s:
    s = s[0].upper() + s[1:].lower() if s[0].isalpha() else s[0] + s[1:].lower()
    print(s)

