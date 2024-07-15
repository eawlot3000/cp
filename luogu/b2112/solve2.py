#!/usr/bin/env python3
n = int(input())
l = []
for i in range(n):
  r = list(map(str, input().split()))
  if r[0] == 'rock':
    r[0] = 'r'

  a = str(r[0][0] + r[1][0]) #print(a)
  l.append(a)
  print(l)

  if a == 'rs' or a == 'pr' or a == 'sp':
    print('Player1') 
  elif a == 'sr' or a == 'rp' or a == 'ps':
    print('Player2')
  else:
    print('Tie')


'''
# wrong one. need to fix a lot
n = int(input())
l = []
for i in range(n):
  r = list(map(str, input().split()))
  a = str(r[0][0] + r[1][0]) #print(a)
  l.append(a)
  print(l)

  if a == 'rs' or a == 'pr' or a == 'sp':
    print('Player1') 
  elif a == 'sr' or a == 'rp' or a == 'ps':
    print('Player2')
  else:
    print('Tie')
'''
