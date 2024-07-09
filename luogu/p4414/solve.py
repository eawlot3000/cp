#!/usr/bin/env python3
seq = list(input().split())
min_num = int(min(seq))
letter = str(input())
mid_arr = seq
mid_arr.remove(min(seq))
mid_arr.remove(max(seq))
min_num = int(mid_arr[0])
ret = []
for i in range(len(letter)):
  if letter[i] == 'A':
    ret += [min_num]
  elif letter[i] == 'C':
    ret += [max(seq)]
  else:
    ret += [min_num]
for j in range(len(ret)-1):
  print(ret[j], end = ' ')
print(ret[-1])
