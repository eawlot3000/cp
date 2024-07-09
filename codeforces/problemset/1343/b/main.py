n = int(input())
for i in range(n):
  all_num = []
  r = int(input())
  for k in range(1, 100):
    all_num += [k]
  ret = [0] * r
  new = []
  for k in range(1, 100):
    ret += [k]
    for j in range(r):
      if ret[int(r/2)] % 2==0:
        new += [ret[int(r/2)]]
        if ret[int(r/2)*2] % 2:

  print(new)



