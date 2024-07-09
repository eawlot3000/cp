n = int(input())
if n != 1:
  s = sorted(map(int, input().split()))[::-1]
  #print('s ------>', s)
  summ, c = 0, 0
  for i in range(len(s)):
    summ += int(s[i])
    c += 1
    #print(summ, c)
    if summ > sum(s[i+1:]):
      print(c)
      break
else:
  print(1)
