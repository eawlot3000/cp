n = int(input())
arr = str(input()).split()
ret = []
count = 1
for i in range(1,n):
  if int(arr[i]) == int(arr[i-1])+1:
    count += 1
  else:
    ret += [count]
    count = 1
ret.append(count)
print(max(ret))
