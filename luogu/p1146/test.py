n = int(input())
ret = [0] * n
print(n)
for i in range(n):
  for j in range(n):
    if j != i:
      if ret[j]:
        ret[j] = 0
      else:
        ret[j] = 1
  count = 0
  for t in ret:
    count += 1
    if count == n:
      count = 0
    print(t,end = '' if count != 0 else '\n')
