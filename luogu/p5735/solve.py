#!/usr/bin/env python3
import math
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1 = math.sqrt((b1-a1)**2 + (b2-a2)**2)
d2 = math.sqrt((c1-a1)**2 + (c2-a2)**2)
d3 = math.sqrt((b1-c1)**2 + (b2-c2)**2)
print('{:.2f}'.format(int(d1+d2+d3)))
