n = int(input())
s = str(input()).split()
odd, even = 0, 0
c_odd, c_even = [], []
for i in range(n):
  if int(s[i])%2:
    odd += 1
    c_odd += [i+1]
  else:
    even += 1
    c_even += [i+1]
if odd > even:
  f = False
else:
  f = True
print(c_odd[0] if f else c_even[0])

