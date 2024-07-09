'''
aa = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
print(sum(aa))
bb = [1, 2, 4, 71, 142]
print(sum(bb))
'''

#n = int(input())
n = 206
def divisor(x):
  calc = 0
  for i in range(1,x):
    if x%i == 0:
      calc += i
  return calc

for i in range(n, n+100):
  for j in range(0, 100):
    if i == divisor(i+j) and i+j == divisor(i):
      break
  print(i, i+j)
# 207 306
