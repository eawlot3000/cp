n = int(input())
arr = str(input()).split()
count = [0]*n
for i in range(len(arr)):
  for j in range(0,i):
    if arr[j] < arr[i]:
      count[i] += 1
for i in count:
  print(i, end = ' ')
