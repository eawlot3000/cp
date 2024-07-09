n = int(input())
s = str(input()).split()
if n!=1:
  count,ret = 0, 0
  for i in range(1, len(s)):
    if int(s[i]) >= int(s[i-1]):
      count += 1
      ret = count if count > ret else ret
    else:
      count = 0 
  print(ret+1)
else:
  print(1)
