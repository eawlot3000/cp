m,n = map(int, input().split())
summ = 0
dd = 0
for i in range(m,n+1):
  if i%17==0:
    summ += i
print('{}'.format(summ))
