arr = []
for i in range(1000):
  i = str(i)
  if i.count('4') + i.count('7') == len(i):
    arr += [int(i)]
s = int(input())
ret = []
for j in arr:
  if s%j == 0:
    ret += ['1']
  else:
    ret += ['0']
if '1' in ret:
  print("YES")
else:
  print("NO")
'''
    if j == '4' or j == '7':
      arr += [int(i)]
'''
