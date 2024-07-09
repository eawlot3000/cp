n = int(input())
x = str(input())
z = str(input())
for i in range(n+1):
  if x[i] < z[i]:
    print('-1')
  else:
    print(z)
  break
