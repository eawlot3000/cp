import math
n = int(input())
print('1', end = ' ')
for i in range(2, int(math.sqrt(n))+1):
  print(i**2, end = ' ')

