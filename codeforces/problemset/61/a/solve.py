s1 = str(input())
s2 = str(input())
for i in range(len(s1)):
  print("{}".format(int(s1[i]) ^ int(s2[i])), end = '')

