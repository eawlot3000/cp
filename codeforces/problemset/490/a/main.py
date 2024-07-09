a = int(input())
n = []
n += map(int, input().split())
cc = min(min(n.count(1), n.count(2)), n.count(3))
if cc != 0:
  for j in range(cc):
    ret, out = [], []
    for i in range(a):
      if n[i] not in ret:
        if i+1 not in out:
          ret += [n[i]]
          out += [i+1]
    print(out)
else:
  print(0)
