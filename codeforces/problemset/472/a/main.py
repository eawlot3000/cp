n = int(input())
ret = []
for i in range(2, n):
  for j in range(2, i):
    if i%j == 0:
      break
  else:
    ret += [i]
  new = []
  for k in range(2,n):
    if k not in ret:
      new += [k]
print(new)
