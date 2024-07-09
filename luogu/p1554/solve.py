# 129 130 131 132 133 134 135 136 137
# count the times that every digit appeared

c0,c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0,0,0,0,0,0,0,0,0,0
a,b = map(int, input().split())
for i in range(a,b+1):
  for j in str(i):
    if j == '0':
      c0 += 1
    elif j == '1':
      c1 += 1
    elif j == '2':
      c2 += 1
    elif j == '3':
      c3 += 1
    elif j == '4':
      c4 += 1
    elif j == '5':
      c5 += 1
    elif j == '6':
      c6 += 1
    elif j == '7':
      c7 += 1
    elif j == '8':
      c8 += 1
    else:
      c9 += 1
ret = []
ret.append(c0)
ret.append(c1)
ret.append(c2)
ret.append(c3)
ret.append(c4)
ret.append(c5)
ret.append(c6)
ret.append(c7)
ret.append(c8)
ret.append(c9)
for s in ret:
  print(s, end = ' ')
