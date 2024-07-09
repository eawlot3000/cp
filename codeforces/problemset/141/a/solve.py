a = str(input())
b = str(input())
c = str(input())
ab = a+b
f = True
if len(ab) != len(c):
  print('NO')
else:
  for i in ab:
    if ab.count(i) == c.count(i):
      continue
    else:
      print('NO')
      f = False
      break
  if f:
    print('YES')
