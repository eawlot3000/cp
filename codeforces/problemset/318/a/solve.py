'''
n, k = map(int, input().split())
if n%2:
  bp = (n-1)//2
else:
  bp = n//2
arr = []
if k < bp:
  for i in range(1, n+1):
    if i%2:
      arr.append(i)
  #print(arr)
  print(arr[k-1])
else:
  arr = []
  for i in range(1, n+1):
    if i%2 == 0:
      arr.append(i)
  #print(arr)
  print(arr[k-bp-1])
  '''

n, k = map(int, input().split())
if k <= (n + 1) // 2:
  result = 2 * k - 1
else:
  result = 2 * (k - (n + 1) // 2)
print(result)
