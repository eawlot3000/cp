n = int(input())
ret = [1]
print('1')
for i in range(n-1):
  ret.append(0)
  ret = [ret[j-1] + ret[j] for j in range(i+2)]
  # so classic this one
  count = 0
  for t in ret:
    count += 1
    if count == i+2:
      count = 0
    print(t,end = ' ' if count != 0 else '\n')
