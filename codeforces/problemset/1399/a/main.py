'''
n = int(input())
for i in range(n):
  a = int(input())
  s = []
  s += map(int, input().split())
  f = []
  for x in range(a):
    for y in range(x, a):
      if abs(s[x]-s[y]) > 1:
        f += [0]
        break
      else:
        f += [1]
  print('YES' if 0 not in f else 'NO')
'''

for i in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  f = True
  for j in range(n):
    for k in range(j+1, n):
      if abs(a[j]-a[k]) > 1:
        f = False
        break
    if not f:
      break
  print('YES' if f else 'NO')
