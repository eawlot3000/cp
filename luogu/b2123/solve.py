#!/usr/bin/env python3
s = input().strip()
if s:
  result = []
  count = 1

  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
    else:
      result.append(str(count))
      result.append(s[i - 1])
      count = 1

  # Append the last sequence
  result.append(str(count))
  result.append(s[-1])

  print(''.join(result))
else:
  print("")





'''
a = str(input())
l = []
c = 0
for i in range(1, len(a)):
  if a[i] == a[i-1]:
    c += 1
    l.append(c)
    l.append(a[i])
  else:
    c = 1
    l.append(c)
    l.append(a[i])
print(l)
'''



'''
a = str(input())
for i in range(len(a)):
  a.count(a[i])
  print(a.count(a[i]), end = ' ')
'''
