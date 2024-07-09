'''
# 1st
def cal(t,a):
  if t%a == 0:
    print('{}'.format(t//a))
  else:
    print('{}'.format((t//a)+1))
  
n,m,a = map(int, input().split())
if n//a>=1 and m//a>=1:
  print('{}'.format((n//a)*2 + 2))
elif n//a>=1 or m//a>=1:
  if n>m:
    cal(n,a)
  else:
    cal(m,a)
    '''
import math
n,m,a = map(int, input().split())
if n>a and m>a:
  print('{}'.format(((n-1)//a+1) * ((m-1)//a+1)))
else:
  print('{}'.format(((n-1)//a+1) * (math.ceil((m-1)//a)+1)))
