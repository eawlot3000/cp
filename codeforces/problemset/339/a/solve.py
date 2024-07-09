s = str(input())
arr = []
for i in range(0, len(s), 2):
  arr.append(int(s[i]))
  arr = sorted(arr)
for j in range(len(arr)-1):
  print(arr[j], end = '+')
print(arr[-1])
