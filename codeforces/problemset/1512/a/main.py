n = int(input())
for i in range(n):
  a, num = int(input()), []
  num += map(int, input().split())
  t = 0
  for j in range(a):
    mad = num[j]
    if num.count(mad) == 1:
      t = num[j]
    if num[j] == t:
      print(j+1)
