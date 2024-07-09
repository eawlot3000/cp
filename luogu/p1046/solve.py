aa = str(input()).split()
n = int(input())
count = 0
for i in range(len(aa)):
  if n+30 >= int(aa[i]):
    count += 1
print(count)
