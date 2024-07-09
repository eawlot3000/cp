#!/usr/bin/env python3
n = int(input())
if n>0:
  print(n)
else:
  print(max(int(n/10), 0-abs(int(str(int((n/100))) + str(n)[-1]))))
  #print(int(n/10), 0-abs(int(str(int((n/100))) + str(n)[-1])))

