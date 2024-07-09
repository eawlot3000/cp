# omg this crap didnt say something?

a,b = input().split()
c = int(a) / int(b)
if int(a) % int(b) != 0:
  print('{:.9}'.format(c))
else:
  print('{}'.format(float(c)))




