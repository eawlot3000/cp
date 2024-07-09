n = int(input())
# omg here!! i can finally doing the multi input! so dumb
ret = list(map(int, input().split()))
arr = [0] * n
for i in range(n):
  arr[i] = ret[i]
print(max(arr) - min(arr))
