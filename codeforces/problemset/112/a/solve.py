s1 = str(input()).lower()
s2 = str(input()).lower()
if s1 == s2:
  print('0')
else:
  print('-1' if s1<s2 else '1')
