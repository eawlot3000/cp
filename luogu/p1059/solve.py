n = int(input())
aa = list(set(input().split()))
for i in range(len(aa)):
  for j in range(i):
    if int(aa[i]) < int(aa[j]):
      temp = 0
      temp = aa[i]
      aa[i] = aa[j]
      aa[j] = temp
print(len(aa))
for i in aa:
  print(i, end = ' ')
