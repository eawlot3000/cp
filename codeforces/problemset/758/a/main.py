n = int(input())
a = []
a += map(int, input().split())
st, al = max(a), 0
for i in range(n):
  al += st - a[i]
print(al)
