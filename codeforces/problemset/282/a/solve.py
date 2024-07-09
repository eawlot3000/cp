o = 0
n = int(input())
for i in range(n):
  s = str(input())
  if s == '++X' or s == 'X++':
    o += 1
  else:
    o -= 1
print(o)
