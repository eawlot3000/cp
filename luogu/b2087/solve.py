n = int(input())
aa = str(input()).split()
m = int(input())
count = 0
for i in aa:
  if int(i) == m:
    count += 1
print(count)
