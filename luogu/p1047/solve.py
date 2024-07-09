l, m = map(int, input().split())
ret = []
for i in range(m):
  aa = str(input()).split()
  ret += [aa[0]]
  ret += [aa[1]]
nums = []
for i in range(0,len(ret),2):
  for j in range(int(ret[i]), int(ret[i+1])+1):
    nums += [j]
print(l-len(set(nums))+1)
