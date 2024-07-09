s = str(input())
rem = ["A", "O", "Y", "E", "U", "I"]
for i in range(len(rem)):
  rem += [rem[i].lower()]
ret = []
for j in range(len(s)):
  if s[j] not in rem:
    ret.append(s[j])
for s in range(len(ret)):
  print('.{}'.format(ret[s].lower()), end = '')
