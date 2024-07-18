#!/usr/bin/env python3
a = str(input()).split()
print(a)
print(len(a))

print(max(a), min(a))


ll, ss = a[0], a[0]
for i in range(len(a)):
  print('word is ', a[i])
  if a[i] > ll:
    ll = a[i]
  elif a[i] < ss:
    ss = a[i]
print(ll, ss)

