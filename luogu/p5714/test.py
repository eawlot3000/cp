m,h = map(float, input().split())
cal = m/h**2
if cal<18.5:
  print('Underweight')
elif 18.5 <= cal < 24:
  print('Normal')
else:
  print('{:.6}'.format(cal))
  print('Overweight')
