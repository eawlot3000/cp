'''
x = int(input())
ret = []
if abs(x) != x:
  print('0')
else:
  x = str(x)
  for i in range(len(x)):
    j = x[-1-i]
    ret.append(j)
  summ = 0
  times = len(x)
  for t in ret:
    summ += int(t) * 10 ** times
    times -= 1
  if int(summ/10) == int(x):
    print('1')
    '''
x = int(input())
print(str(x) == str(x)[::-1])


'''
x = int(input())
ret = []
x = str(x)
for i in range(len(x)):
  j = x[-1-i]
  ret.append(j)
summ = 0
times = len(x)
for t in ret:
  summ += int(t) * 10 ** times
  times -= 1
if str(summ/10) == str(x):
    print('right')
    '''
