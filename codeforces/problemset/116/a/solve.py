n = int(input())
ret = []
summ = 0
for i in range(n):
  raw = str(input()).split()
  summ -= int(raw[0])
  summ += int(raw[-1])
  ret += [summ]
print(max(ret))
