#!/usr/bin/env python3
numbers = []
for i in range(1, 354294): # why this number? 9^5 * 6 = 354294
  di = [int(x) for x in str(i)]
  temp = sum(d ** 5 for d in di)
  if temp == i:
    numbers.append(i)
    print(">>>> temp >>>>", temp)
print(sum(numbers)-1)
