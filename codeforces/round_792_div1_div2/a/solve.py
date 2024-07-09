n = int(input())
ret = [0] * n
out = [0] * n
for i in range(n):
  ret[i] = str(input())
  if len(ret[i]) > 2:
    out[i] = min(ret[i])
  if len(ret[i]) == 2:
    out[i] = max(ret[i])
  if len(ret[i]) == 1:
    out[i] = int(ret[i])
  print(out[i])
