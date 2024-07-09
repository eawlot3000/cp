n,k = map(int, input().split())
count = 0
for i in range(n,k+1):
  i = str(i)
  count += i.count('2')
print(count)
