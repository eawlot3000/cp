n, x = map(int, input().split())
cnt = 0
raw = str(input()).split()
for i in range(len(raw)):
  if int(raw[i]) == 0:
    continue
  if int(raw[i]) >= int(raw[x-1]):
    cnt += 1
print(cnt)
