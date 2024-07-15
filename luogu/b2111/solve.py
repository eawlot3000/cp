#!/usr/bin/env python3
n = float(input())
n, a, b = float(input()), list(str(input())), list(str(input()))
print('yes' if n <= sum([1 for i in range(len(a)) if a[i] == b[i]])/len(a) else 'no')





'''
n = float(input())

a = list(str(input()))
b = list(str(input()))
#a = list(map(str, input().split()))
#b = list(map(str, input().split()))
#print(a, b)
#print(a[0])

c = 0
for i in range(len(a)):
  #print(a[i], b[i])
  if a[i] == b[i]:
    c += 1
#print(c)
val = c/len(a)
#print(val)

if n <= val:
  print('yes')
else:
  print('no')
'''
