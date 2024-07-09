c, r = map(int, input().split())
com_line = "#" * r
dot_line = "."*(r-1) + "#"
re = False
for i in range(c):
  if i%2==0:
    print(com_line)
  else:
    if re:
      print(dot_line[::-1])
      re = False
    else:
      print(dot_line)
      re = True
