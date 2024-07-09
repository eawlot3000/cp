n = int(input())
ret = []
for i in range(n):
  num = int(input())
  ret.append(num)
for i in range(n):
  print(int(ret[i]-ret[i]//8))
