n = int(input())
import math
if n%2:
  print("-{}".format(math.ceil(n/2)))
else:
  print(int(n/2))

'''
summ = 0
f = False
for i in range(1, n+1):
  if f:
    summ += i
    f = False
  else:
    summ -= i
    f = True
print(summ)
'''
