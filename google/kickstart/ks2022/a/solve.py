import sys
from sys import stdin

def get_strs():
  return map(str, sys.stdin.readline().strip().split())

n = int(input())
for i in range(n):
  get_strs(s1, s2)
  if set(s1) == set(s2):
    print("Case #{}: {}".format(i+1, len(s2) - len(s1)))
  else:
    print("Case #{}: IMPOSSIBLE".format(i+1))


'''
n = int(input())
ret = []
nums = []
for i in range(n):
  s1 = str(input())
  s2 = str(input())
  if set(s1) == set(s2):
    ret += [True]
    nums += [len(s2) - len(s1)]
  else:
    ret += [False]
for i in range(n):
  if ret[i] == True:
    print("Case #{}: {}".format(i+1, nums[i]))
  else:
    print("Case #{}: IMPOSSIBLE".format(i+1))
'''
