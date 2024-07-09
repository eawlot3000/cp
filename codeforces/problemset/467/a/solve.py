n = int(input())
count = 0
for i in range(n):
  s = str(input()).split()
  if int(s[1]) - int(s[0]) >= 2:
    count += 1
print(count)
