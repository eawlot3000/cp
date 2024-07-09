'''
ret, arr = [], []
count = 0
ret = input().split()
for i in ret:
  arr += [int(i)]
for i in range(len(arr)):
  for j in range(i-1):
    if arr[i] == arr[j]:
      del arr[-1]
      count += 1
print(count, arr)
'''

nums = [0,0,1,1,1,2,2,3,3,4]
dd = nums
length = int(len(nums))

ret = [0] * len(set(nums))
nums = list(set(nums))
for i in range(len(set(nums))):
  ret[i] = nums[i]
for j in range(length - len(set(nums))):
  ret.extend('_')
print(len(set(dd)), str(ret).replace("'", '').replace(' ', ''), end = ' ')
