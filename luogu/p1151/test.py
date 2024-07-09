k = int(input())

state = False
#ret = []
while True:
  for i in range(10000,30001):
    #ret += [i]
    # check number(output) is c
    sub1 = int(i/100) #worked
    sub2 = int((i - int(i/10000)*10000)/10) #worked
    sub3 = int(i%1000) #worked
    #compare = sub1%k + sub2%k + sub3%k
    if sub1%k + sub2%k + sub3%k == 0:
      print(i)
      #state=True
  break
print('No')
#if state==False:
#  print('No')

