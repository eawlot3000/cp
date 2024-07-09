# https://www.luogu.com.cn/problem/B2044
a,b,c = map(int, input().split())
if a<60 and b>=60 and c>=60:
  print('1')
elif a>=60 and b<60 and c>=60:
  print('1')
elif a>=60 and b>=60 and c<60:
  print('1')
else:
  print('0')


