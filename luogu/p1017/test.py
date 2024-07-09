##### !!!! -20 ≤ R ≤ −2 // |n| ≤ 37336

# convert base 10 to base -2
# first try: lets do the basic
'''
import math
math.ceil()
math.floor()
'''
# ok.. this one only works with float e.g. math.floor(2.9) --> 2

n,r = map(int, input().split()) # notice: r<0
integer = n

aa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J']
ret = []

# new code part i: --> fix the base-16
#if abs(r) < 10:
# new code ends

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

# new code pt ii: --> exit if
#else:
# now fix the abs(r)>10 part


ret.reverse()
for i in ret:
#out = ''.join(str(i) for i in ret)
  print(aa[i]) # 110001: one number in single line

# test to be done: -15 -2 --> 110001
# worked !!!


print('{}={}(base{})'.format(integer, aa[i], r))


