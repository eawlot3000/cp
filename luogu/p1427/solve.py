new = str(input()).split()
new.reverse()
for i in range(1,len(new)-1):
  print(new[i], end = ' ')
print(new[-1])
