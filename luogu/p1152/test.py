import gc
ret = list(map(int,input().split()))
arr = [0] * 1000000100
pp = []
for i in range(ret[0]):
  arr[i] = ret[i+1]
  pp += [abs(arr[i] - arr[i-1])%ret[0]]
arr.sort()
arr = list(set(arr))
if arr[0] == 0:
  del arr[0]
  gc.collect()
pp = list(set(pp))
if len(arr) > len(pp):
  del arr[-1]
if pp == arr:
  print('Jolly')
else:
  print('Not jolly')


'''
  for j in range(i):
    if pp[j-1] >= pp[j]:
      pp[j-1], pp[j] = pp[j], pp[j-1]

pp = list(set(pp))
if len(arr) > len(pp):
  arr.pop(-1)
  #del arr[-1]
if pp == arr:
  print('jolly')
else:
  print('not jolly')
'''
