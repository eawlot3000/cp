#!/usr/bin/env python3
a = str(input())
for i in range(1, len(a)):
  o = int(a[i]) + int(a[i-1])
  print(chr(o+96), end='')
  #print(o)
print(chr(int(a[0])+int(a[-1])+96))


'''
a = 'e' 
b = 101
print(ord(a)-96)
print(chr(b))


a = 5 + 96
print(chr(a))
'''
