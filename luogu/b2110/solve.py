#!/usr/bin/env python3
a = str(input())
for i in a:
  if a.count(i) == 1:
    print(i)
    break
else:
  print("no")
