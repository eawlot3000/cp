n = int(input())
ret = []
sum1, sum2, sum3 = 0, 0, 0
for i in range(n):
  raw = str(input()).split()
  sum1 += int(raw[0])
  sum2 += int(raw[1])
  sum3 += int(raw[2])

if sum1 == sum2 == sum3 == 0:
  print("YES")
else:
  print("NO")
