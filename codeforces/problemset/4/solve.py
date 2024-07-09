n = int(input())
s = False
for i in range(1,n+1):
  if int(n-i)%2==0 and i%2==0:
    s = True
    break
if s:
  print("YES")
else:
  print("NO")

n = int(input())
if n%2 == 0 and n != 2:
  print('YES')
else:
  print('NO')
