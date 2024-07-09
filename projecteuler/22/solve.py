import sorted
ll = sorted.namell
#print(ll[937])
s = 0
ss = 0
for i in range(len(ll)):
  for j in range(len(ll[i])):
    s += ord(ll[i][j]) - 64
  ss += (i+1) * s
  s = 0 #reset it !!!
    #print(ll[i][j], ord(ll[938][i]) - 64)
  #print(ord('Z') - 64)
  # print(ll[938][i])

print(s)
print(ss)
