n = int(input())
wo = []
if n!=1:
  for i in range(1,n):
    if i%2:
      wo.append('hate')
    else:
      wo.append('love')
  for j in range(1,n):
    if j%2:
      print("I {} that".format(wo[0]), end = ' ')
    else:
      print("I {} that".format(wo[1]), end = ' ')
  if n%2:
    print('I hate it')
  else:
    print('I love it')
if n == 1:
  print('I hate it')
