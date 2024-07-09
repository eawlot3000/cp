import math
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
print('{:.3f}'.format(math.sqrt((x1-x2)**2 + (y1-y2)**2)))
