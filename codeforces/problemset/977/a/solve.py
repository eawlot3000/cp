n, t = map(int, input().split())
for i in range(t):
  if str(n)[-1] != '0':
    n -= 1
  else:
    n /= 10
    n = int(n)
    n = int(n)
print(n)
