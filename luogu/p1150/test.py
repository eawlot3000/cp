# n>1 , k<=10**8
n,k = map(int,input().split())
num = n
count = 1
if n/k>=2:
  while n-k>=k:
    out = n-k
    n = out+1
    count += 1
  print(num+count)

else:
  print(n+1)


