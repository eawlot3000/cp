n, time = map(int, input().split())
c, left = 0, 240-time
for i in range(1, n+1):
  if left - i*5 >= 0:
    c += 1
  left -= i*5
print(c)
