a = str(input())
up, low = 0, 0
for i in range(len(a)):
  if a[i].isupper():
    up += 1
  else:
    low += 1
if low < up:
  print(a.upper())
else:
  print(a.lower())
