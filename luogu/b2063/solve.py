a,b = map(int,input().split())
for i in range(b):
  pop = 1.001*a
  a = pop
print('{:.4f}'.format(a))
