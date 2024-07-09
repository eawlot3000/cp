n = int(input())
arr = []
for i in range(n):
  s = str(input())
  arr += [s]
count = 1
for j in range(1,len(arr)):
  if arr[j][0] != arr[j-1][-1]:
    continue
  else:
    count += 1
if count == 1:
  if n == 1 or len(arr) != len(set(arr)):
    print(1)
  else:
    print(2)
else:
  print(count)
