a, b = map(int, input().split())
ret = []
ret += map(int, input().split())
c, p = 0, 0
for i in range(a):
  ret[i] += b
  if ret[i] <= 5:
    c += 1
    if c == 3:
      p += 1
      c = 0
print(p)
