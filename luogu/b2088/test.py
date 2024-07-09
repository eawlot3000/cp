#!/usr/bin/env python3
price = '28.9 32.7 45.6 78 35 86.2 27.8 43 56 65'
aa = str(input()).split()
summ = float(0)
for i in range(len(aa)):
  ss = float(aa[i]) * float(price.split()[i])
  summ += ss
print('{:.1f}'.format(summ))
