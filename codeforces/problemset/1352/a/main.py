n = int(input())
ret = []
for i in range(n):
  ret += [int(input())]
part = 0
print('---')
for i in range(n):
  #print(ret[i] % 10)
  #print(ret[i] % (10**(len(str(ret[i]))-1)))
  if len(str(ret[i]))==1:
    print(f'1\n{ret[i]}')
  if ret[i] % 10 == 0:
    print(f'1\n{ret[i]}')
  else:
    out, c = [], 0
    while ret[i] > 10:
      out += [ret[i] - (ret[i] % (10**(len(str(ret[i]))-1)))]
      ret[i] -= (ret[i] % (10**(len(str(ret[i]))-1)))
    print(out)
    # how to do this??




#print(ret[i])
