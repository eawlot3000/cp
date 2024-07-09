k,n,w = map(int, input().split())
cost, am = 0, 1
for i in range(1,w+1):
  am = k*i
  cost += am
print(cost-n if cost-n>0 else 0)
