a,b,c,d = map(int, input().split())
ret = [a,b,c,d]
summ = max(a,b,c,d)
ret.remove(summ)
print(summ-ret[0], summ-ret[1], summ-ret[-1])
