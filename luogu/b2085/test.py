import math
n = int(input())
ret = []
for num in range(2,4000000):
  if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
    ret.append(num)
#print(ret[n-1])
print(ret[30000])
