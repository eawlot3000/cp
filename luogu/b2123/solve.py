#!/usr/bin/env python3
a = str(input())
l = []
c = 0
for i in range(1, len(a)):
  if a[i] == a[i-1]:
    c += 1
    l.append(c)
    l.append(a[i])
  else:
    c = 1
    l.append(c)
    l.append(a[i])
print(l)



'''
a = str(input())
for i in range(len(a)):
  a.count(a[i])
  print(a.count(a[i]), end = ' ')
'''
