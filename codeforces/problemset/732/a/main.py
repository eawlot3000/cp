a, b = map(int, input().split())
s, i = True, 1
while s:
  if i*a%10==0 or (i*a-b)%10==0:
    print(i)
    s = False
  i += 1
