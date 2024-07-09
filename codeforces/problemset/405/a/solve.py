n = int(input())
s = list(input().split())
arr = []
for i in range(len(s)):
  arr += [int(s[i])]
arr = sorted(arr)
for i in range(len(arr)):
  print(int(arr[i]), end = ' ')
