# 1st
n = int(input())
ret = []
for i in range(n):
  m = int(input())
  ret += [m]
for t in range(n):
  if ret[t]%2 == 0:
    print('pb wins')
  else:
    print('zs wins')

# try 2nd
'''
n = int(input())
ret = []
for i in range(n):
  m = int(input())
  if m%2:
    ret[i] = 'zs wins'
  else:
    ret[i] = 'pb wins'

  
print(ret)
'''
