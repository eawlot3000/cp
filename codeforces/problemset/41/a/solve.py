og = list(input())
og.reverse()
com = list(input())
if og == com:
  print("YES")
else:
  print("NO")

'''
if og == com:
  print("NO")
else:
  if sorted(og) == sorted(com):
    print("YES")
  else:
    print("NO")
'''
