#!/usr/bin/env python3

dic = {}
n = int(input())
for i in range(n):
  score, name = input().split()
  dic[name] = int(score)

print(max(dic, key=dic.get))
