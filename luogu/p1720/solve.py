import math
n = int(input())
sq = math.sqrt(5)
out = ((1+sq)/2)**n - ((1-sq)/2)**n 
print('{:.2f}'.format(out/sq))
