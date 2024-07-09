n = int(input())
sx = str(input()).split()
sy = str(input()).split()
sx.remove(sx[0])
sy.remove(sy[0])
arr = sy + sx
check = []
for i in range(1,n+1):
  check += [str(i)]
if sorted(check) == sorted(set(arr)):
  print("I become the guy.")
else:
  print("Oh, my keyboard!")

