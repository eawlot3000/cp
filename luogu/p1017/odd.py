# !/bin/python3

# those are odds numbers
ret = []
for bin(i) in range(100):
  if i&1 == 1:
    ret += [i]
print(ret)

print('----')

# wait ???????
# those are even numbers
ret1 = []
for bin(x) in range(100):
  ''' if x&1 != 1:'''
  if x|0 == 0:
    ret1 += [x]
print(ret1)


