'''
n = int(input())
aa = str(input()).split()
aa.reverse()
for i in aa:
  print(i, end = ' ')
  '''
# ---- another wave ----
n = int(input())
aa = str(input()).split()
for i in range(len(aa)):
  print(aa[-1-i], end = ' ')
