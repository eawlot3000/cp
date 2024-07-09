n = int(input())
arr = input().split()
ret = []
for s in range(len(arr)):
  ret = arr
print(ret)
for i in range(n):
  for j in range(1,i-1):
    if ret[i] == ret[j]:
      del ret[j]
print(ret)

'''
for i in set(ret):
  print(i,end = ' ')
'''
