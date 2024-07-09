ret = [0, 0]
for i in range(5):
  aa = str(input()).split()
  for j in range(5):
    if aa[j] == '1':
      ret[0] = int(i+1)
      ret[1] = int(j+1)
cnt = 0
while ret[0] != 3:
  if ret[0] < 3:
    ret[0] += 1
    cnt += 1
  if ret[0] > 3:
    ret[0] -= 1
    cnt += 1
while ret[1] != 3:
  if ret[1] < 3:
    ret[1] += 1
    cnt += 1
  if ret[1] > 3:
    ret[1] -= 1
    cnt += 1
print(cnt)
