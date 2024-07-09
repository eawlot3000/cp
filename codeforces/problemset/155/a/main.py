s, n, c = [], int(input()), 0
s += map(int, input().split())
mi, ma = s[0], s[0]
for i in range(1, len(s)):
  if s[i] < mi:
    mi = s[i]
    c += 1
  if s[i] > ma:
    ma = s[i]
    c += 1
print(0) if len(s) == 1 else print(c)
