# https://www.luogu.com.cn/problem/B2047
def cal(x):
  if 0<=x<5:
    y = -x+2.5
  elif 5<=x<10:
    y = 2-1.5*(x-3)*(x-3)
  else:
    y = x/2-1.5
  return y
x = float(input())
print('{:.3f}'.format(cal(x)))



