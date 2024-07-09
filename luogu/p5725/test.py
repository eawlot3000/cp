n = int(input())
for i in range(1,n**2+1):
 if i%n == 0:
    print("%02d"%i)
  else:
    print("%02d"%i, end = '')
print()


count = 1
for i in range(1, n+1):
  print(" " * (n-1)*2, end='') # oh what is this??
  for s in range(1, i+1):
    if s==i:
      print("%02d"%count)
    else:
      #print("{:>{}}".format(count,2*n)) # todo
      print("%02d"%count, end='')
    count += 1
