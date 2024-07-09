n = int(input())
arr = []
for i in range(n):
  ss = str(input()).split()
  arr += [ss[0]]
  arr += [ss[1]]
ret = []
for i in range(1, len(arr), 2):
  for j in range(1000):
    if (int(arr[i-1]) + j) % int(arr[i]) == 0:
      ret.append(j)
      break
for i in ret:
  print(i)
