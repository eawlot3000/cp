'''
n, r = map(int, input().split())

# aa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J']
ret = []
integer = n

while True:
  p = n//r

  if n%1 == 1:
    p += 1
  else:
    p == p 
  mod = abs(n%r)
  ret += [mod]
  if p == 0:
    break
  n = p
ret.reverse()


out = ''.join(str(i) for i in ret)
print(out)
'''




n,r = map(int, input().split())

integer = n
ret = []
while True:
  p = n//r
  # now check is p a odd or even
  if n&1==1:
    p += 1
  else:
    p = p
  mod = abs(n%r)
  ret += [mod]
  if p == 0:
    break
  n = p
ret.reverse()

out = ''.join(str(i) for i in ret)
# test to be done: -15 -2 --> 110001
# worked !!!

print('{}={}(base{})'.format(integer, out, r))

