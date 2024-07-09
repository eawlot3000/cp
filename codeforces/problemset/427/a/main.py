n = int(input())
s, a, c, summ, po = [], 0, 0, 0, 0
s += map(int, input().split())
for i in range(n):
  if s[i] > 0:
    po += int(s[i])
  elif s[i] == -1:
    po -= 1
  if po < 0:
    c += 1
    po = 0
print(c)
