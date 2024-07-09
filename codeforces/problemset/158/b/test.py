n = int(input())
s = str(input()).split()
for i in range(s.count('4')):
  s.remove('4')
new = []
for i in range(len(s)):
  new.append(int(s[i]))
new = sorted(new)
# what changed new --> 1,1,2,2,3,3
ret = 0
for i in range(len(new)):
  summ = new[i] 
  for j in range(i+1, len(new)):
    summ += new[j]
    if summ == 4:
      ret += 1
      summ = 0
print(ret)
