#!/usr/bin/env python3
n = int(input())
cards = list(map(int, input().split()))

count_0 = cards.count(0)
count_5 = cards.count(5)

if count_0 == 0:
  print(-1)
elif count_5 < 9:
  print(0 if count_0 > 0 else -1)
else:
  count_5 = (count_5 // 9) * 9
  result = '5' * count_5 + '0' * count_0
  print(result)

