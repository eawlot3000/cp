n = int(input())
ret = []
for i in range(n):
  num = str(input())
  t = num
  for j in range(1,10):
    num = t
    num = int(str(j) + str(num))
    print(num)
    if num%9==0:
      ret += [num]
print(ret)
