n = int(input())
if n < 150:
  print('{:.1f}'.format(n*0.4463))
elif 150 < n < 400:
  print('{:.1f}'.format(150*0.4463 + (n-150)*0.4663))
else:
  print('{:.1f}'.format(150*0.4463 + 250*0.4663 + (n-400)*0.5663))
