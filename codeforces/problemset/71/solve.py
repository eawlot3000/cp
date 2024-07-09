n = int(input())
ret = []
for i in range(n):
  ret += [str(input())]
for i in range(len(ret)):
  if len(ret[i]) <= 10:
    print(ret[i])
  else:
    print('{}{}{}'.format(ret[i][0], len(ret[i])-2, ret[i][-1]))
