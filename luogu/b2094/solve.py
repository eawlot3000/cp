n = int(input())
arr = int(input().split())
ret = []
for i in range(n):
  ret = arr
ret.remove(max(ret))
summ = 0
for i in ret:
  i = int(i)
  summ += i
print(summ)


