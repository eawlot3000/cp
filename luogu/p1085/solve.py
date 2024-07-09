aa = []
for i in range(7):
  in1 = str(input()).split()
  aa += [int(in1[0])]
  aa += [int(in1[1])]
day, count = [], []
for i in range(1,len(aa)+1,2):
  if aa[i-1] + aa[i] > 8:
    day += [int((i+1)/2)]
    count += [aa[i-1]+aa[i]]

print(day, count)
if len(set(count)) != len(count):

else:
  for i in range(1,len(count)):
    maxout = count[0]
    if count[i-1] > count[i]:
      maxout = count[i-1]
  print(count)
