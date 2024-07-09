n = int(input())
s = str(input()).split()
aa = [0] * n
for i in range(n):
  num = int(s[i])
  aa[num-1] = i+1
for j in aa:
  print(j, end = ' ')
