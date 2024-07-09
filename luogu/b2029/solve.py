import math
h,r = map(int, input().split())
v = r*r*3.14*h/1000
print(math.ceil(20/v))
