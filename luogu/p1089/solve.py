aa = [0] * 12
for i in range(12):
  aa[i] = int(input())
#print(aa)
left = 0
for_save = 0
mom = 0
for i in range(len(aa)):
  for_save += (300-aa[i])
  left = 300-aa[i]
  if left+300 < aa[i]:
    print('-{}'.format(i+1))
    break
  if for_save >= 100:
    for_save -= 100
    mom += 100
  print(for_save)

