s = str(input())
cnt = 0
for i in range(len(s)):
  if int(s[i]) == 4 or int(s[i]) == 7:
    cnt += 1
if cnt == 4 or cnt == 7:
  print('YES')
else:
  print('NO')
