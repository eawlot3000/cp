n = int(input())
for i in range(n):
  s = str(input())
  ret = s[0:2]
  for i in range(3, len(s)+1, 2):
    if s[i-1] == ret[-1]:
      ret += s[i]
    else:
      ret += s[i-1]
      ret += s[i]
  print(ret)
