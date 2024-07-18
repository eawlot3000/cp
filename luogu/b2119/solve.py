#!/usr/bin/env python3
a = str(input()).strip()
if a[-3:] == 'ing':
  print(a[:-3])
elif a[-2:] == 'ly' or a[-2:] == 'er':
  print(a[:-2])
else:
  print(a)


'''
a = str(input())
print(a[:-3] if a[-3:] == 'ing' else a[:-2])
'''
