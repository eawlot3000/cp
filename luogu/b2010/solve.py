"""
a,b = input().split()

out = int(a) / int(b)

if out != 0:
  out = int(a) // int(b)
  leftnum = int(a) - int(b) * int(out)
  print('{} {}'.format(int(out), int(leftnum)))
else:
  print('{} {}'.format(int(out), 0))
  """


a,b = input().split()

left = int(a) % int(b)
out = int(a) // int(b)

if left != 0:
  print('{} {}'.format(int(out), int(left)))
else:
  print('{} {}'.format(int(out), 0))


