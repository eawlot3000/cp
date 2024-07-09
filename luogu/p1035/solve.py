# k: 1<k<15

k = int(input())
ret = []
for i in range(2,50):
  ret += [i]

for t in range(ret[0],ret[47]):
  sn = 1 + 1/t
  compare = sn - k
  print(t)
  #out = k - 1 - 1/t
  #while out<0:
  #  break
  if compare < 1:
    break
#print('{}'.format(ret[t]))
print(compare)  





