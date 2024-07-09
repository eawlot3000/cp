x, n = map(int, input().split())
out = 0
for i in range(x,x+n): # ref starts
  if 1<=i%7<=5:
    out += 250 # ref ends
print(out)
'''
for i in range(x,n+x):
  if i > 7:
    day += [i%7]
  else:
    day += [i]
day.remove(6)
day.remove(7)
print(250*len(day))
'''
