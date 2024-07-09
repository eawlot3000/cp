# n seems more important
m,n = map(int, input().split())
n = str(n)
state = 0
t = len(n) - 1
for i in range(0, len(n)):
  if n[i] != '0':
    if state:
      print("+{}*{}^{}".format(n[i],m,t), end = '')
    else:
      print("{}*{}^{}".format(n[i],m,t), end = '')
      state = 1
  t -= 1

# 1*2^4+1*2^2+1*2^0
