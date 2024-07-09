import math
a,b,c = map(float, input().split())

sqrt = int(math.sqrt(b**2 - 4*a*c))
if sqrt>=0:
  x1 = (-b+sqrt)/a*2
  x2 = (-b-sqrt)/a*2
  
  if x1 == x2:
    print('x1=x2={:.5f}'.format(x1))
  else:
    if x1<x2:
      print('x1={:.5f};x2={:.5f}'.format(x1,x2))
    else:
      print('x1={:.5f};x2={:.5f}'.format(x2,x1))
else:
  print('No answer!')


