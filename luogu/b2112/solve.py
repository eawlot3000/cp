#!/usr/bin/env python3
n = int(input())
l = []
for i in range(n):
  l.append(list(map(str, input().split())))
  l[i][0] = str(l[i][0][0]).lower()
  l[i][1] = str(l[i][1][0]).lower()
#print(l)

for i in range(n):
  if l[i][0] == l[i][1]:
    print('Tie')
  if l[i][0] == 'r' and l[i][1] == 's':
    print('Player1')
  elif l[i][0] == 'r' and l[i][1] == 'p':
    print('Player2')
  if l[i][0] == 'p' and l[i][1] == 'r':
    print('Player1')
  elif l[i][0] == 'p' and l[i][1] == 's':
    print('Player2')
  if l[i][0] == 's' and l[i][1] == 'p':
    print('Player1')
  elif l[i][0] == 's' and l[i][1] == 'r':
    print('Player2')





'''
r -> s -> 1
r -> rest -> 2
p -> r -> 1
p -> rest -> 2
s -> p -> 1
s -> rest -> 2




'''
