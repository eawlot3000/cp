n, h = map(int, input().split())
raw = str(input()).split()
w = 0
for i in range(n):
  if int(raw[i]) > h:
    w += 2
  else:
    w += 1
print(w)
