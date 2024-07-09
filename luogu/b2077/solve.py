n = int(input())
def odd(x):
  cal_odd = x*3+1
  return int(cal_odd)
def even(x):
  return int(x)
if n == 1:
  print('End')
else:
  while True:
    if n%2:
      print('{}*3+1={}'.format(n,n*3+1))
      print('{}/2={}'.format(odd(n),int(odd(n)/2)))
      n = int(odd(n)/2)
    else:
      print('{}/2={}'.format(even(n),int(even(n)/2)))
      n = int(even(n)/2)
    if n == 1:
      print('End')
      break
