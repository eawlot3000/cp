n = int(input())
summ = 0
for i in range(1,n):
  for j in range(1,i):
    print(i)
    print('the', j, 'times')
    summ += i
print(summ)
