#!/usr/bin/env python3

def getnum(OG):
  return OG - 64

li = []
for i in range(2):
  l = 1
  word = str(input())
  for j in word:
    l *= getnum(ord(j))
    print(l)
  l %= 47
  li += [l]

print("GO" if li[0] == li[1] else "STAY")

#print(getnum(ord('A')))
