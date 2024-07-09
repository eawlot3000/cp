#!/usr/bin/env python3
# correct

li = []
for i in range(5):
  li += [list(map(int, input().split()))]
n, m = map(int, input().split())
li[n-1], li[m-1] = li[m-1], li[n-1]

for i in range(5):
  print(' '.join(map(str, li[i])))

''' thoughts
li = []
for i in range(5):
  li += [list(map(int, input().split()))]

print(li)

n, m = map(int, input().split())
print(n, m)

li[n-1], li[m-1] = li[m-1], li[n-1]
print(li)

for i in range(5):
  print(' '.join(map(str, li[i])))
'''
