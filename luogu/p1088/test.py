t1, t2 = map(int, input().split())
def swap(a, b):
  temp = a
  a = b
  b = temp
  return a,b
for i in swap(t1,t2):
  print(i, end = ' ')
