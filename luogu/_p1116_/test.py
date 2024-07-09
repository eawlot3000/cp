'''
n = int(input())
arr = [0] * n
ret = list(map(int,input().split()))
for i in range(n):
  arr[i] = ret[i]
count = 0
for i in range(n):
  for j in range(1,n):
    if arr[j-1] > arr[j]:
      arr[j-1], arr[j] = arr[j], arr[j-1]
      count += 1
print(count)
'''

#runtime error?
n = int(input())
ret = list(map(int,input().split()))
count = 0
for i in range(n):
  arr = ret
for i in range(0,n):
  for j in range(0,n):
    if arr[i] < arr[j]:
      count += 1
print(count)
