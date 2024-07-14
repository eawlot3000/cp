#!/usr/bin/env python3
def is_num(s):
  numlist = ['0','1','2','3','4','5','6','7','8','9']
  return True if s in numlist else False
a = str(input())
c = 0
for i in a:
  if i.isdigit():
    c += 1
  '''
  if is_num(i):
    c += 1
  '''
print(c)
