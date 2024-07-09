#m, n = map(int, input().split())

m = 6
n = 3
arr = [1] * n

state = False
ret = []
for i in range(n):
  for j in range(1, n+20):
    arr[i] = j
    if int(sum(arr)) == m:
      state = True
if state: 
  print(arr)

