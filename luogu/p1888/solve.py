import math
ret = []
'''
a,b,c = map(int, input().split())
ret += [a]
ret += [b]
ret += [c]
'''
ss = str(input()).split()
out = int(min(ss)) / int(max(ss))
if out == 1:
  print('1')
else:
  gcd = math.gcd(int(min(ss)), int(max(ss)))
  # your og!! gcd = int(math.gcd(int(min(ss)), int(max(ss))))
  min_num = int(min(ss))/gcd
  max_num = int(max(ss))/gcd
  print('{}/{}'.format(int(min_num), int(max_num)))
  #print('{}/{}'.format(min(ss), max(ss)))
