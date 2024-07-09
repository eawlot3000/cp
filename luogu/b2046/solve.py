# https://www.luogu.com.cn/problem/B2046
# compare which one gives a less t(time): t = s/v

dis = int(input())
t_bike = dis/3 + 50
t_walk = dis/1.2
if t_bike < t_walk:
  print('Bike')
elif t_walk < t_bike:
  print('Walk')
else:
  print('All')
