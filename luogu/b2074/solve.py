a,b = map(int, input().split())
out = pow(a,b)
if out%7 == 0:
  print('Sunday')
elif out%7 == 1:
  print('Monday')
elif out%7 == 2:
  print('Tuesday')
elif out%7 == 3:
  print('Wednesday')
elif out%7 == 4:
  print('Thursday')
elif out%7 == 5:
  print('Friday')
elif out%7 == 6: 
  print('Saturday')
