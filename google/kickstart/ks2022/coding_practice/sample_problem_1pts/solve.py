n = int(input())
ret = []
for i in range(n):
  data = str(input()).split()
  can = map(int, input().split())
  ret += [sum(can)%int(data[-1])]
for j in range(n):
  print("Case #{}: {}".format(j+1, ret[j]))
